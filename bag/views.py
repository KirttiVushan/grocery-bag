from grocery_bag.views import logIn
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render , reverse
from django.contrib.auth import logout
from .models import Groceries
from django.contrib.auth.models import User
from .forms import Groceries_list
# Create your views here.

def index(request):
    if request.method=='GET':
        groceries=Groceries.objects.filter(user=request.user).order_by('-date')
        return render(request, 'index.html' , {'groceries':groceries})

    else:
        date_filter = request.POST['date']
        groceries=Groceries.objects.filter(date=date_filter)
        return render(request, 'index.html' , {'groceries':groceries , 'date_filter': date_filter})


def add(request):
    if request.method=='GET':
        return render(request , 'add.html' , {'form':Groceries_list()})
    else:
        try:
            new_item = Groceries_list(request.POST)
            profile = new_item.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('bag:index')
        except ValueError:
            return render(request, 'add.html', {'form':new_item , 'error':'please fill all the fields'})


    

def update(request,item_pk):
    groceries = get_object_or_404(Groceries, pk=item_pk , user=request.user)
    if request.method == 'GET':
        form=Groceries_list(instance=groceries)
        return render (request , 'update.html' , {'groceries':groceries , 'form':form})
    else:
        try:
            form=Groceries_list(request.POST, instance=groceries)
            form.save()
            return redirect('bag:index')
        except ValueError:
            return render(request, 'update.html', {'groceries':groceries , 'form':form , 'error':'please fill all the fields'})


def delete_item(request,item_pk):
    groceries=get_object_or_404(Groceries, pk=item_pk , user=request.user)
    if request.method=='POST':
        groceries.delete()
        return redirect('bag:index')
    else:
        return render(request, 'index.html',{'groceries':groceries})


def logOut(request):
    if request.method=='POST':
        logout(request)
        return redirect(logIn)