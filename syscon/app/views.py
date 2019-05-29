from django.shortcuts import render, get_object_or_404, redirect
from .models import Function, Collaborator, Resident, Schedule
from .forms import FunctionForm, CollaboratorForm

# Create your views here.

def dashboard(request):
    return render(request, 'app/dashboard.html', {})

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

#

def collaborator(request):
    collaborators = Collaborator.objects.all()
    return render(request, 'app/collaborator.html', {'collaborators':collaborators})

def collaborator_new(request):
     if request.method == "POST":
         form = CollaboratorForm(request.POST)
         if form.is_valid():
             collaborator = form.save(commit=False)
             author = request.user
             collaborator.save()
             return redirect('collaborator')
     else:
        form = CollaboratorForm()
     return render(request, 'app/collaborator_edit.html', {'form': form})

def collaborator_edit(request, pk):
     collaborator = get_object_or_404(collaborator, pk=pk)
     if request.method == "POST":
         form = CollaboratorForm(request.POST, instance=collaborator)
         if form.is_valid():
             collaborator = form.save(commit=False)
             author = request.user
             collaborator.save()
             return redirect('collaborator')
     else:
        form = CollaboratorForm(instance=collaborator)
     return render(request, 'app/collaborator_edit.html', {'form': form})

def collaborator_delete(request, pk):
    collaborator = get_object_or_404(collaborator, pk=pk)
    collaborator.delete()
    return redirect('collaborator')

#

def resident(request):
    residents = Resident.objects.all()
    return render(request, 'app/resident.html', {'residents':residents})

def resident_detail(request, pk):
    resident = get_object_or_404(Resident, pk=pk)
    return render(request, 'app/resident_detail.html', {'resident': resident})

def schedule(request):
    schedules = Schedule.objects.all()
    return render(request, 'app/schedule.html', {'schedules':schedules})

def schedule_detail(request, pk):
    schedule = get_object_or_404(Schedule, pk=pk)
    return render(request, 'app/schedule_detail.html', {'schedule': schedule})

def about(request):
    return render(request, 'app/about.html', {})

def login(request):
    return render(request, 'app/login.html', {})

def register(request):
    return render(request, 'app/register.html', {})