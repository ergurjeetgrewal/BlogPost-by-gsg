from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('desc', '')
        if len(name)<2 or len(email)<10 or len(phone)<10 or len(msg)<20:
            messages.error(request,"Please Fill form correctly")
        else:
            contactsave = Contact(name=name,email=email,phone=phone,desc=msg)
            contactsave.save()
            messages.success(request,"Your Form has been sent successfully")
        return render(request, 'home/contactus.html')
    return render(request, 'home/contactus.html')

def search(request):
    query = request.GET['search']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPoststitle=Post.objects.filter(title__icontains=query)
        allPostscontent=Post.objects.filter(content__icontains=query)
        allPosts=allPoststitle.union(allPostscontent)
    if allPosts.count() == 0:
        messages.warning(request,"No result found please refine your query")
    params={'allPosts':allPosts,'query':query}
    return render(request, 'home/search.html',params)