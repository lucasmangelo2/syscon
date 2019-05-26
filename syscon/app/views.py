from django.shortcuts import render
from .models import Function, Collaborator, Resident

# Create your views here.

def dashboard(request):
    return render(request, 'app/dashboard.html', {})


def function(request):
    functions = Function.objects.all()
    return render(request, 'app/function.html', {'functions':functions})


def collaborator(request):
    collaborators = Collaborator.objects.all()
    return render(request, 'app/collaborator.html', {'collaborators':collaborators})


def resident(request):
    residents = Resident.objects.all()
    return render(request, 'app/resident.html', {'residents':residents})

def about(request):
    return render(request, 'app/about.html', {})

def login(request):
    return render(request, 'app/login.html', {})

def register(request):
    return render(request, 'app/register.html', {})

def schedule(request):
    return render(request, 'app/schedule.html', {})