from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('function', views.function, name='function'),
    path('collaborator', views.collaborator, name='collaborator'),
    path('resident', views.collaborator, name='resident'),
]