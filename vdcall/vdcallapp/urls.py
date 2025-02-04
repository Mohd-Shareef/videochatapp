from django.contrib import admin
from django.urls import path
from vdcallapp import views

urlpatterns = [
    path('register/', views.register,name='register'),
    path('', views.login_view,name='Login'),
    path('home/', views.home,name='home'),
    path('videocall/', views.videocall,name='videocall'),
    path('join/',views.join_room, name='join_room'),
    path('logout/', views.logout_view,name='logout'),
]
