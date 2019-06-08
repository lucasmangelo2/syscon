from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.decorators import login_required
from .models import Function, Collaborator, Resident, Schedule
from .forms import FunctionForm, CollaboratorForm, ScheduleForm
import json
from django.core import serializers


# Create your views here.

def dashboard(request):
    return render(request, 'app/dashboard.html', {})

# Function

@login_required
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

def function_export(request):
    functions = Function.objects.all()
    data ={"data":  get_json_list(functions)}
    return JsonResponse(data)

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

def collaborator_export(request):
    collaborators = Collaborator.objects.all()

    for item in collaborators:
        item.author = None
        item.function = None

    data ={"data":  get_json_list(collaborators)}
    return JsonResponse(data)

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

def schedule_export(request):
    schedules = Schedule.objects.all()

    for item in schedules:
        item.author = None
        item.collaborator = None

    data ={"data":  get_json_list(schedules)}
    return JsonResponse(data)


# About

def about(request):
    return render(request, 'app/about.html', {})


def get_json_list(query_set):
    list_objects = []
    for obj in query_set:
        dict_obj = {}
        for field in obj._meta.get_fields():
            try:
                if field.many_to_many:
                    dict_obj[field.name] = get_json_list(getattr(obj, field.name).all())
                    continue
                dict_obj[field.name] = getattr(obj, field.name)
            except AttributeError:
                continue
        list_objects.append(dict_obj)
    return list_objects