from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.user_signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('profile/', views.user_profile, name='profile'),
    path('update-user/', views.user_profile, name='UpdateUser'),
    path('add-task/', views.addTask, name='AddTask'),
    path('tasks/', views.home, name='ListTasks'),
    path('task/<str:slug>/edit', views.editTask, name='EditTask'),
    path('task/<str:slug>/delete', views.deleteTask, name='DeleteTask'),
]