"""
URL configuration for FitShare project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from fitShareApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home_page, name="home_page"),
    path('create_program/', views.create_program, name="create_program"),
    path('login/', views.login, name="login"),
    path('show_program/', views.show_program, name="show_program"),
    path('about', views.about, name="about")
]
