from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.models import Post, Blogcomment
from django.contrib import messages
from blog.templatetags import get_dict
# Create your views here.


def index(request):
    allposts = Post.objects.all()
    context = {'allposts': allposts}
    return render(request, 'blog/index.html', context)


def blogPost(request, slug):
    posts = Post.objects.filter(slug=slug).first()
    comments = Blogcomment.objects.filter(post=posts, parent=None)
    Replies = Blogcomment.objects.filter(post=posts).exclude(parent=None)
    repDict = {}
    for reply in Replies:
        if reply.parent.sno not in repDict.keys():
            repDict[reply.parent.sno] =[reply]
        else:
            repDict[reply.parent.sno].append(reply)
    if posts != None:
        context = {'post': posts, 'comments': comments,'repDict':repDict}
    else:
        return HttpResponse('error')
    return render(request, 'blog/blogpost.html', context)


def postcomment(request):
    if request.method == "POST":
        comment = request.POST.get('comment')
        user = request.user
        postSno = request.POST.get('postSno')
        post = Post.objects.get(s_no=postSno)
        parentSno = request.POST.get("parentSno")
        if parentSno == None:
            csave = Blogcomment(comment=comment, user=user, post=post)
            csave.save()
            messages.success(
                request, "your comment has been posted successfully")
        else:
            parent = Blogcomment.objects.get(sno=parentSno)
            csave = Blogcomment(comment=comment, user=user,
                                post=post, parent=parent)
            csave.save()
            messages.success(
                request, "your reply has been posted successfully")
    return redirect(f'/blog/{post.slug}')
