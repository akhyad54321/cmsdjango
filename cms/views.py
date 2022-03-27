from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .forms import CmsForm
from .models import Company
from django.utils import timezone
from django.contrib.auth.decorators import login_required


# Create your views here.
def home(request):
    return render(request, 'home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                return redirect('home')
            except IntegrityError:
                return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'That username has already been taken. Please choose a new username'})
        else:
            return render(request, 'signupuser.html', {'form':UserCreationForm(), 'error':'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form':AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form':AuthenticationForm(), 'error':'Username and password did not match'})
        else:
            login(request, user)
            return redirect('home')

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required
def addCompany(request):
    if request.method == 'GET':
        return render(request, 'addCompany.html', {'form':CmsForm()})
    else:
        try:
            form = CmsForm(request.POST)
            print(form)
            newCompany = form.save(commit=False)
            newCompany.user = request.user
            newCompany.save()
            return redirect('myCompany')
        except ValueError:
            return render(request, 'addCompany.html', {'form':CmsForm(), 'error':'Bad data passed in. Try again.'})

@login_required
def listCompany(request):
    companies = Company.objects.filter(user=request.user)
    return render(request, 'listcompany.html', {'companies':companies})

@login_required
def edit(request, edit_pk):
    edit_company = get_object_or_404(Company, pk=edit_pk, user=request.user)
    if request.method == 'GET':
        form = CmsForm(instance=edit_company)
        return render(request, 'viewtodo.html', {'edit_company':edit_company, 'form':form})
    else:
        try:
            form = CmsForm(request.POST, instance=edit_company)
            form.save()
            return redirect('myCompany')
        except ValueError:
            return render(request, 'edit.html', {'edit_company':edit_company, 'form':form, 'error':'Bad info'})


@login_required
def deletecompany(request, company_pk):
    todo = get_object_or_404(Company, pk=company_pk, user=request.user)
    if request.method == 'POST':
        todo.delete()
        return redirect('myCompany')