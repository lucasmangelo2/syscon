from django.shortcuts import render, redirect
from .forms import AuthenticateForm, RegisterUserForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as lg, logout

# Create your views here.

def login(request):
    message = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                lg(request, user)
                return redirect('dashboard')
            else:
                message = 'Usuário desativado'
        else:
            message = 'Usuáro ou senha incorretos'
    
    form = AuthenticateForm()

    return render(request, 'core/login.html', {'form':form, 'message':message})

def authenicate(request):
    return render(request, 'core/login.html', {})

def register(request):
    message = None
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        
        user = User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
    

    form = RegisterUserForm()
    return render(request, 'core/register.html', {'form':form, 'message':message})

def logout_view(request):
    logout(request)
    return redirect('dashboard')