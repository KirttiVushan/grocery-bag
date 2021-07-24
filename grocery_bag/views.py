from django.http import request
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout , authenticate



def logIn(request):
    if request.method=='GET':
        return render(request, 'login.html',{'form':AuthenticationForm()})
    else:
        user=authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'login.html', {'form':AuthenticationForm(), 'error':'No username registered'})
        else:
            login(request,user)
            return redirect('bag:index')


def signIn(request):
    if request.method == 'GET':
        return render(request, 'signin.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('logIn')
            except:
                return render(request, 'signin.html',{'form':UserCreationForm(), 'error':'The username is already taken, try something different'})
        else:
            return render(request,'signin.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

