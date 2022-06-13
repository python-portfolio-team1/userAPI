from .models import Users
from urllib import response
from django.conf import settings
from rest_framework import status
from django.shortcuts import render
from django.core.mail import send_mail
from .serializers import UsersSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import HttpResponseRedirect



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

# Create your views here


def send_email(request, to):
    subject = 'SIDEHUSTLE PYTHON PORTFOLIO TEAM API'
    message = ' DREY TAKE YOUR PROJECT '
    email_from = settings.EMAIL_HOST_USER
    # recipient_list = ['receiver@gmail.com',]
    recipient_list = to
    send_mail( subject, message, email_from, recipient_list )
    return HttpResponseRedirect('redirect to a new page')

from django.contrib.auth import authenticate,login ,logout 
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

def signup(request):

    if request.user.is_authenticated:
        return HttpResponseRedirect('/books')
    
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            if form:
                send_email(request, form.cleaned_data['username'])      # sending mail upon regsitration
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username,password = password)
            login(request, user)
            return HttpResponseRedirect('/login')
        
        else:
            return render(request,'itemsapp/signup.html',{'form':form})
    
    else:
        form = UserCreationForm()
        return render(request,'itemsapp/signup.html',{'form':form})


def signin(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/login')
    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username =username, password = password)

        if user is not None:
            login(request,user)
            return HttpResponseRedirect('/signup')
        else:
            form = AuthenticationForm()
            return render(request,'itemsapp/signin.html',{'form':form})
    
    else:
        form = AuthenticationForm()
        return render(request, 'itemsapp/signin.html', {'form':form})


def signout(request):
    logout(request)
    return HttpResponseRedirect('/.../signin/')

