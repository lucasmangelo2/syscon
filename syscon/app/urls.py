from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('function', views.function, name='function'),
    path('collaborator', views.collaborator, name='collaborator'),
    path('resident', views.resident, name='resident'),
    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('schedule', views.schedule, name='schedule'),
]