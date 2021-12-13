from django.shortcuts import render
from blog1.models import Post,Category
# Create your views here.

def home(request):
    posts=Post.objects.all()
    category=Category.objects.all()
    context={'posts':posts,'category':category}
    return render(request,'blog1/home.html',context)

def postcategory(request,slug):
    category=Category.objects.filter(slug=slug).first()
    posts=Post.objects.filter(category=category)
    context={'posts':posts}
    return render(request,"blog1/postcategories.html",context)

def postdetail(request,slug):
    post=Post.objects.filter(slug=slug).first()
    context={'post':post}
    return render(request,'blog1/postdetails.html',context)
