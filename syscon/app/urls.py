from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('function', views.function, name='function'),
    #path('function/<int:pk>/', views.function_detail, name='function_detail'),
    path('function/new', views.function_new, name='function_new'),
    path('function/<int:pk>/edit/', views.function_edit, name='function_edit'),
    path('function/<int:pk>/delete/', views.function_delete, name='function_delete'),

    path('collaborator', views.collaborator, name='collaborator'),
    #path('collaborator/<int:pk>/', views.collaborator_detail, name='collaborator_detail'),
    path('collaborator/new', views.collaborator_new, name='collaborator_new'),
    path('collaborator/<int:pk>/edit/', views.collaborator_edit, name='collaborator_edit'),
    path('collaborator/<int:pk>/delete/', views.collaborator_delete, name='collaborator_delete'),

    path('resident', views.resident, name='resident'),
    path('resident/<int:pk>/', views.resident_detail, name='resident_detail'),

    path('schedule', views.schedule, name='schedule'),
    path('schedule/<int:pk>/', views.schedule_detail, name='schedule_detail'),

    path('about', views.about, name='about'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
]