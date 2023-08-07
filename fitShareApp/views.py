from django.shortcuts import render, redirect
from .models import User, Training_Program, Exercise
from .forms import *
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def home_page(request):
    # if not request.user.is_authenticated:
    #     return redirect('sign_in')
    programs = Training_Program.objects.all()
    return render(request, 'home_page.html', {'programs':programs})


def add_training_program(request):
    custom_user = request.user
    if custom_user.is_authenticated:
        user = User.get_user_by_email(custom_user.email)
    else:
        return redirect('login_user')

    if request.method == "POST":
        form = AddTrainingProgramForm(request.POST, initial={'user_id':user})
        if form.is_valid():
            form.save()
            return redirect('home_page')
    elif request.method == "DELETE":
        raise Http404()
    else:
        form = AddTrainingProgramForm(initial={'user_id': user})
    
    return render(request, 'add_trining_program.html', {"user":user, "form":form})


def edit_training_program(request):
    pass


def delete_training_program(request):
    pass

def sign_up(request):
    pass

def login_user(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                messages.info(request, "Username OR password is incorrect")
    return render(
        request,
        "login_user.html",
    )

def logout_user(request):
    pass

def show_program(request):
    pass

def about(request):
    pass
