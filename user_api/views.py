from django.shortcuts import render
import email
from .models import Users
from django.urls import reverse
from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'user_api/index.html')

def login(request):
    return render(request, 'user_api/login.html')

def profile(request):
    return render(request, 'user_api/profile.html')


def addrecord(request):
    f = request.POST['firstname']
    l = request.POST['lastname']    
    e = request.POST['email']
    b = request.POST['birthday']
    m = request.POST['phone']
    a = request.POST['address']
    p = request.POST['password']
    user = user(firstname=f, lastname=l, email=e, birthday=b, phone=m, address=a, password=p)
    user.save()
    return HttpResponseRedirect(reverse('profile'))

def delete(request, id):
    user = Users.objects.get(id=id)    
    user.delete()
    return HttpResponseRedirect(reverse('index'))

def update(request, id):
    user = Users.objects.get(id=id)
    context = {
        'user': user,
    }
    return render(request, "user_api/profile.html", context)

def updaterecord(request, id):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    emial = request.POST['email']  
    phone = request.POST['phone']  
    birtday = request.POST['birthday']  
    address = request.POST['address']  
    user = Users.objects.get(id=id)
    user.firstname = firstname
    user.lastname = lastname
    user.email = email
    user.save()
    return HttpResponseRedirect(reverse('profile'))
