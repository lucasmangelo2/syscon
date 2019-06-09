import json
import os
from django.http import HttpResponse, JsonResponse, Http404
from django.core.serializers.json import DjangoJSONEncoder
from django.conf import settings
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from .models import Function, Collaborator, Resident, Schedule
from .forms import FunctionForm, CollaboratorForm, ScheduleForm
from zipfile import ZipFile

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
    data = get_json_list(functions)
    
    response = export_zip_file(request, 'function_export', 'function.json',data)
    return response

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

    data = get_json_list(collaborators)
    
    response = export_zip_file(request, 'collaborator_export', 'collaborator.json',data)
    return response

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

    data = get_json_list(schedules)
    
    response = export_zip_file(request, 'schedule_export', 'schedules.json',data)
    return response

def schedule_conclude(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk) 
    schedule.status = 'C'
    schedule.save()

    return redirect('schedule')

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
                else:
                    value = getattr(obj, field.name)

                    if field.is_relation:
                        value = value.__str__()
                
                dict_obj[field.name] = value

            except AttributeError:
                continue
        list_objects.append(dict_obj)

    return json.dumps(list_objects,sort_keys=True,indent=1, cls=DjangoJSONEncoder)

def export_zip_file(request, zipname, filename, content):
    try:
        from BytesIO import BytesIO
    except ImportError:
        from io import BytesIO

    in_memory = BytesIO()
    zip = ZipFile(in_memory, "a")
        
    zip.writestr(filename, content)
    
    # fix for Linux zip files read in Windows
    for file in zip.filelist:
        file.create_system = 0    
        
    zip.close()

    response = HttpResponse(content_type="application/zip")
    response["Content-Disposition"] = "attachment; filename={0}.zip".format(zipname)
    
    in_memory.seek(0)    
    response.write(in_memory.read())

    return response