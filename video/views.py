from django.core.checks import messages
from django.db.models.query_utils import PathInfo
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from video.models import Category, Item, VideoComment
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def categorylist(request):
    categories = Category.objects.all()
    context={'categories':categories}
    return render(request, 'video/categorylist.html',context)

def categoryvideos(request,slug):
    print('category')
    category=Category.objects.filter(slug=slug).first()
    catvideos = Item.objects.filter(category=category)
    context={'catvideos':catvideos}
    return render(request,'video/catvideo.html',context)

def videodetail(request,slug):
    video=Item.objects.filter(slug=slug).first()
    comments=VideoComment.objects.filter(video=video,parent=None)
    replies=VideoComment.objects.filter(video=video).exclude(parent=None)
    repDict={}
    for reply in replies:
        print(reply.comment)
        if reply.parent.id not in repDict.keys():
            repDict[reply.parent.id]=[reply]
        else:
            repDict[reply.parent.id].append(reply)

        print(reply)
        print(reply.parent.id)
    context = {'videos':video,'comments':comments,'user':request.user,'repDict':repDict}
    
    return render(request,'video/videodetail.html',context)

def videocomment(request):
    if request.method == 'POST':
        videocomment=request.POST['comment']
        user=request.user
        videosno=request.POST['videoSno']
        video=Item.objects.get(id=videosno)
        print(video)
        parentsno=request.POST['parentSno']
        if parentsno=="":
            comment1=VideoComment(comment=videocomment,user=user,video=video)      
            comment1.save()
            messages.success(request,"Your Comment has been posted successfully")
            return HttpResponseRedirect(reverse('video:videodetail',args=(video.slug,)))
        else:
            print('parent')
            parent=VideoComment.objects.get(id=parentsno)
            comment1=VideoComment(comment=videocomment,user=user,video=video,parent=parent) 
            comment1.save()
            messages.success(request,"Your reply has been added")
            return HttpResponseRedirect(reverse('video:videodetail',args=(video.slug,)))





