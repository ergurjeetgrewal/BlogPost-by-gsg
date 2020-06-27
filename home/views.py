from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
# Create your views here.


def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    res = False
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        msg = request.POST.get('desc', '')
        contactsave = Contact(name=name,email=email,phone=phone,desc=msg)
        contactsave.save()
        res  =True
        return render(request, 'home/contactus.html',{"res":res})
    return render(request, 'home/contactus.html')
