from django.contrib import admin
from django.urls import path, include
from authentication import views

urlpatterns = [
    path('', views.home, name= "home"),
    path('index', views.index, name= "index"),
    path('signup', views.signup, name= "signup"),
    path('landing', views.landing, name= "landing"),
    # path('', views.InsertRecord, name= "InsertRecord")
]
