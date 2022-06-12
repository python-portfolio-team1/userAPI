# import email
from .models import Users
from urllib import response
from django.urls import reverse
from django.conf import settings
from rest_framework import status
from django.shortcuts import render
from django.core.mail import send_mail
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect, JsonResponse



@api_view(['GET', 'POST'])
def users_list(request):

    if request.method == 'GET':
        users = Users.objects.all()
        serializer = UsersSerializer(users, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = UsersSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
 
@api_view(['GET', 'PUT', 'DELETE'])
def users_detail(request):

    try:
        users = Users.object.get(pk=id)
    except Users.DoesNotExist:
        return response(status=status.HTTP_404_NOT_FOUND)    

    if request.method =='GET': 
        serializer = UsersSerializer(users)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = UsersSerializer(users, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)        
    elif request.method =='DELETE':
        users.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

from django.http import HttpResponseRedirect

# Create your views here.

def index(request):
    return render(request, 'user_api/index.html')

def login(request):
    return render(request, 'user_api/login.html')

def profile(request):
    return render(request, 'user_api/profile.html')

def send_email(request):
    subject = 'SIDEHUSTLE PYTHON PORTFOLIO TEAM API'
    message = ' DREY TAKE YOUR PROJECT '
    email_from = settings.EMAIL_HOST_USER
    recipient_list = ['receiver@gmail.com',]
    send_mail( subject, message, email_from, recipient_list )
    return redirect('redirect to a new page')

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
