from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone
# Create your models here.

class Function(models.Model):
    name = models.CharField(max_length=200)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Collaborator(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    birth_day = models.DateTimeField()
    function = models.ForeignKey('Function', on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Apartament(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    owner = models.ForeignKey('auth.User', on_delete=models.PROTECT, related_name='%(class)s_owner')    
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    birth_day = models.DateField()
    number = models.IntegerField()

    def __str__(self):
        return self.name

class Resident(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    birth_day = models.DateField()
    initial_day = models.DateField()
    ending_day = models.DateField()
    apartament =  models.ForeignKey('Apartament', on_delete=models.PROTECT)   

    def __str__(self):
        return self.name

class Schedule(models.Model):
    author= models.ForeignKey('auth.User', on_delete=models.PROTECT)
    created_date = models.DateTimeField(default=timezone.now)
    name = models.CharField(max_length=200)
    date = models.DateField()
    collaborator = models.ForeignKey('Collaborator', on_delete=models.CASCADE)