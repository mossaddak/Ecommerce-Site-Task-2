from django.contrib import admin
from django.urls import path,include
from .import views

urlpatterns = [
    path('siungIn/', views.SingIn, name="siungIn"),
    path('SingUp/', views.SingUp, name="SingUp"),
    path('Logout/', views.Logout, name="Logout"),
    path('Dashboard/', views.Dashboard, name="Dashboard"),
    path('ChangeProfilePicture/', views.ChangeProfilePicture, name="ChangeProfilePicture"),
    path('ForgetPassword/', views.ForgetPassword, name="ForgetPassword"),
    path('ChangePassword/<token>/', views.ChangePassword, name="ChangePassword"),
]
