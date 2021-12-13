from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from .models import Item,Category,VideoComment
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def categorylist(request):
    print("categoryist is called")
    categories=Category.objects.all()
    context={'categories':categories}
    return render(request,'video/categorylist.html',context)


def categoryvideos(request,slug):
    print("category is called")
    category=Category.objects.filter(slug=slug).first()
    catvideos=Item.objects.filter(category=category)
    context={'catvideos':catvideos}
    return render(request,'video/catvideo.html',context)

def videodetail(request,slug):
    print("videodetail is called")
    video=Item.objects.filter(slug=slug).first()
    comments=VideoComment.objects.filter(video=video,parent=None)
    replies=VideoComment.objects.filter(video=video).exclude(parent=None)
    repDict={}
    for reply in replies:
        if reply.parent.srno not in repDict.keys():
            repDict[reply.parent.srno]=[reply]
        else:
            repDict[reply.parent.srno].append(reply)
    context={'videos':video,'comments':comments,'user':request.user,'repDict':repDict}
    # print(repDict)
    # print(comments)
    return render(request,'video/videodetail.html',context)

def comments(request):
    
    
        
    videocomment=request.POST.get('commentbox')
    user=request.user
    videosno=request.POST.get('videoSno')
    print(videosno)
    video=Item.objects.get(id=videosno)
    parentSno=request.POST.get('parentSno')
    if parentSno == "":
        comment1=VideoComment(comment=videocomment,user=user,video=video)
        comment1.save()
        messages.success(request,"Your comment has been posted")
        return HttpResponseRedirect(reverse('video:videodetail',args=(video.slug,)))
    else:
        parent=VideoComment.objects.get(srno=parentSno)
        comment1=VideoComment(comment=videocomment,user=user,video=video,parent=parent)
        comment1.save()
        messages.success(request,"Your reply has been added")
        return HttpResponseRedirect(reverse('video:videodetail',args=(video.slug,)))


