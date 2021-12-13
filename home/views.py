from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
from blog1.models import Post
from home.models import Contact

def homepage(request):
    return render(request,'home/index.html')

def signup(request):
    if request.method=='POST':
        firstname=request.POST['first_name']
        lastname=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password1']
        cpassword=request.POST['password2']
        email=request.POST['email']
        if firstname=="":
            messages.error(request,"First name is must")
            return redirect('/register')
        elif lastname=="":
            messages.error(request,"Last Name is must")
            return redirect('/register')
        elif username=="":
            messages.error(request,"Username is must")
            return redirect('/register')
        elif len(username)>7:
            messages.error(request,"Username should not be more than 7 characters")
            return redirect('/register')
        elif password=="":
            messages.error(request,"Password is must")
            return redirect('/register')
        elif cpassword=="":
            messages.error(request,"Confirm Password is must")
            return redirect('/register')
        elif email=="":
            messages.error(request,"Email is must")
            return redirect('/register')
        elif password!=cpassword:
            messages.error(request,"Password didn't match")
            return redirect('/register')
        else:
            if User.objects.filter(username=username).exists():
                messages.error(request,"Username not available")
                return redirect("/register")
            elif User.objects.filter(email=email).exists():
                messages.error(request,"Email already exists")
                return redirect("/register")
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=firstname,last_name=lastname)
                user.save()
                messages.info(request,"Registered Successfully")
                auth.login(request,user)
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
        
                    return redirect('/')
    else:
        return render(request,'home/register.html')
    

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        net=request.POST['next']
        print(username,password,net)
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.info(request,"Login Successful")
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
        
                return redirect('/')
        else:
            messages.error(request,"Check Username or Password")
            return redirect('/login')
    else:
        return render(request,'home/login.html')

def logout(request):
    auth.logout(request)
    return redirect("/")

def contactus(request):
    if request.method=='POST':
        name=request.POST['name']
        username=request.POST['username']
        msg=request.POST['message']
        email=request.POST['email']
        contact=request.POST['contact']
        c=Contact(name=name,username=username,contactno=contact,email=email,msg=msg)
        c.save()
        messages.success(request,"Thanks for contacting.We will get back soon")
        return redirect('/contact')
    else:
        return render(request,'home/contact.html')
    

def search(request):
    query=request.GET['query']
    if(len(query)>60):
        posts=Post.objects.none()
    else:
        posttitles=Post.objects.filter(title__icontains=query)
        postcontents=Post.objects.filter(desc__icontains=query)
        posts=posttitles.union(postcontents)
    if posts.count()==0:
        messages.warning(request,"No search result found")
    context={'posts':posts,'query':query}

    return render(request,"home/search.html",context)