from django.shortcuts import render, get_object_or_404, redirect
from .models import Function, Collaborator, Resident, Schedule
from .forms import FunctionForm, CollaboratorForm, ScheduleForm

# Create your views here.

def dashboard(request):
    return render(request, 'app/dashboard.html', {})

# Function

def function(request):
    functions = Function.objects.all()
    return render(request, 'app/function.html', {'functions':functions})

def function_new(request):
     if request.method == "POST":
         form = FunctionForm(request.POST)
         if form.is_valid():
             function = form.save(commit=False)
             function.save()
             return redirect('function')
     else:
        form = FunctionForm()
     return render(request, 'app/function_edit.html', {'form': form})

def function_edit(request, pk):
     function = get_object_or_404(Function, pk=pk)
     if request.method == "POST":
         form = FunctionForm(request.POST, instance=function)
         if form.is_valid():
             function = form.save(commit=False)
             function.save()
             return redirect('function')
     else:
        form = FunctionForm(instance=function)
     return render(request, 'app/function_edit.html', {'form': form})

def function_delete(request, pk):
    function = get_object_or_404(Function, pk=pk)
    function.delete()
    return redirect('function')

# Collaborator

def collaborator(request):
    collaborators = Collaborator.objects.all()
    return render(request, 'app/collaborator.html', {'collaborators':collaborators})

def collaborator_new(request):
     if request.method == "POST":
         form = CollaboratorForm(request.POST)
         if form.is_valid():
             collaborator = form.save(commit=False)
             collaborator.author = request.user
             collaborator.save()
             return redirect('collaborator')
     else:
        form = CollaboratorForm()
     return render(request, 'app/collaborator_edit.html', {'form': form})

def collaborator_edit(request, pk):
     collaborator = get_object_or_404(Collaborator, pk=pk)
     if request.method == "POST":
         form = CollaboratorForm(request.POST, instance=collaborator)
         if form.is_valid():
             collaborator = form.save(commit=False)
             collaborator.author = request.user
             collaborator.save()
             return redirect('collaborator')
     else:
        form = CollaboratorForm(instance=collaborator)
     return render(request, 'app/collaborator_edit.html', {'form': form})

def collaborator_delete(request, pk):
    collaborator = get_object_or_404(Collaborator, pk=pk)
    collaborator.delete()
    return redirect('collaborator')

# Schedule

def schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'app/schedule.html', {'schedules':schedules})

def schedule_new(request):
     if request.method == "POST":
         form = ScheduleForm(request.POST)
         if form.is_valid():
             schedule = form.save(commit=False)
             schedule.author = request.user
             schedule.save()
             return redirect('schedule')
     else:
        form = ScheduleForm()
     return render(request, 'app/schedule_edit.html', {'form': form})

def schedule_edit(request, pk):
     schedule = get_object_or_404(Schedule, pk=pk)
     if request.method == "POST":
         form = ScheduleForm(request.POST, instance=schedule)
         if form.is_valid():
             schedule = form.save(commit=False)
             schedule.author = request.user
             schedule.save()
             return redirect('schedule')
     else:
        form = ScheduleForm(instance=schedule)
     return render(request, 'app/schedule_edit.html', {'form': form})

def schedule_delete(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    schedule.delete()
    return redirect('schedule')

# About

def about(request):
    return render(request, 'app/about.html', {})