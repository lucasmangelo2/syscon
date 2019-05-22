from django.shortcuts import render
from .models import Function, Collaborator

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
    return render(request, 'app/resident.html', {})