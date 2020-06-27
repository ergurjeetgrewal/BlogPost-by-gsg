from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages
from blog.models import Post
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
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
        if len(name) < 2 or len(email) < 10 or len(phone) < 10 or len(msg) < 20:
            messages.error(request, "Please Fill form correctly")
        else:
            contactsave = Contact(name=name, email=email,
                                  phone=phone, desc=msg)
            contactsave.save()
            messages.success(request, "Your Form has been sent successfully")
        return render(request, 'home/contactus.html')
    return render(request, 'home/contactus.html')


def search(request):
    query = request.GET['search']
    if len(query) > 78:
        allPosts = Post.objects.none()
    else:
        allPoststitle = Post.objects.filter(title__icontains=query)
        allPostscontent = Post.objects.filter(content__icontains=query)
        allPosts = allPoststitle.union(allPostscontent)
    if allPosts.count() == 0:
        messages.warning(request, "No result found please refine your query")
    params = {'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def handlesignup(request):
    if request.method == "POST":
        Username = request.POST['Username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        # checking username exists
        auser = User.objects.filter(username=Username)
        print(auser)
        if auser.count() != 0:
            messages.error(request, "Username Already exists")
            return redirect('/')
        aemail = User.objects.filter(email=email)
        if aemail.count() != None:
            messages.error(request, "Email Already exists")
            return redirect('/')
        # error checking
        if len(Username) > 10 or len(Username) < 5:
            messages.error(
                request, "Username must be between 5-10 letters/digits")
            return redirect('/')
        if not Username.isalnum():
            messages.error(
                request, "Username Should not contain special charaters")
            return redirect('/')
        if password != cpassword:
            messages.error(request, "Password Did not match")
            return redirect('/')
        # user creation
        newuser = User.objects.create_user(Username, email, password)
        newuser.first_name = fname
        newuser.last_name = lname
        newuser.save()
        messages.success(
            request, "Please check your email id for verification")
        return redirect('/')
    else:
        return HttpResponse('404 Not found')


def handlelogin(request):
    if request.method == "POST":
        luser = request.POST['luser']
        lpassword = request.POST['lpassword'] 
        user = authenticate(username=luser,password=lpassword)
        if user is not None:
            login(request,user)
            messages.success(request, "Logged in successfully")
            return redirect('/')
        else:
            messages.error(request, "Invalid Credentials,Please try again")
            return redirect('/')
    return redirect('/')


def handlelogout(request):
    if request.method=="POST":
        logout(request)
        messages.success(request, "successfully logged out")
        return redirect('/')
    return redirect('/')
