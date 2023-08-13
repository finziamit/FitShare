from django.shortcuts import render, redirect
from .models import User, Training_Program, Exercise
from .forms import *
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist


def home_page(request):
    programs = Training_Program.objects.all()
    return render(request, 'home_page.html', {'programs':programs})


def add_training_program(request):
    custom_user = request.user
    if custom_user.is_authenticated:
        user = User.get_user_by_email(custom_user.username)
    else:
        return redirect('login_user')

    if request.method == "POST":
        form = AddTrainingProgramForm(request.POST, initial={'user_id': user})

        if form.is_valid():
            program = form.save()

            exercise_prefix = 'exercises'
            exercise_count = 1
            while f"{exercise_prefix}-{exercise_count}-name" in request.POST:
                exercise_name = request.POST[f"{exercise_prefix}-{exercise_count}-name"]
                sets = int(request.POST[f"{exercise_prefix}-{exercise_count}-sets"])
                reps = int(request.POST[f"{exercise_prefix}-{exercise_count}-reps"])

                exercise = Exercise.create_exercise(name=exercise_name, sets=sets, reps=reps)
                program.excercises.add(exercise)

                exercise_count += 1

            program.save()

            return redirect('home_page')

    else:
        form = AddTrainingProgramForm(initial={'user_id': user})

    return render(request, 'add_training_program.html', {"user": user, "form": form})



def edit_training_program(request):
    pass


def delete_training_program(request, training_program_pk):
    try:
        program = Training_Program.objects.get(id=training_program_pk)
        user = program.user_id
        program.delete()
        return redirect(home_page)

    except Training_Program.DoesNotExist:
        raise Http404()

def signup(request):
    if request.user.is_authenticated:
        return redirect('home_page')

    registration_attempt = False
    if request.method == 'POST':
        registration_attempt = True
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account created successfully')
            return redirect('login_user')
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = NewUserForm()
    return render(request, 'signup.html', {'register_form': form, 'registration_attempt': registration_attempt})

def login_user(request):
    if request.user.is_authenticated:
        return redirect("home_paage")
    else:
        if request.method == "POST":
            username = request.POST.get("email")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home_page")
            else:
                messages.info(request, "Username OR password is incorrect")
    return render(
        request,
        "login_user.html",
    )


def logout_user(request):
    logout(request)
    return redirect("login_user")

def show_program(request, program_pk):
    try:
        program = Training_Program.objects.get(pk=program_pk)
    except ObjectDoesNotExist:
        raise Http404()
    
    return render(request, 'show_training_program.html', {'program': program})


def about(request):
    return render(request, 'about.html', {})
