from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('function', views.function, name='function'),
    path('function/new', views.function_new, name='function_new'),
    path('function/<int:pk>/edit/', views.function_edit, name='function_edit'),
    path('function/<int:pk>/delete/', views.function_delete, name='function_delete'),

    path('collaborator', views.collaborator, name='collaborator'),
    path('collaborator/new', views.collaborator_new, name='collaborator_new'),
    path('collaborator/<int:pk>/edit/', views.collaborator_edit, name='collaborator_edit'),
    path('collaborator/<int:pk>/delete/', views.collaborator_delete, name='collaborator_delete'),

    path('schedule', views.schedule, name='schedule'),
    path('schedule/new', views.schedule_new, name='schedule_new'),
    path('schedule/<int:pk>/edit/', views.schedule_edit, name='schedule_edit'),
    path('schedule/<int:pk>/delete/', views.schedule_delete, name='schedule_delete'),

    path('about', views.about, name='about'),
]