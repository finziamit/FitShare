from django.shortcuts import render, redirect
from .models import User, Training_Program, Exercise

def home_page(request):
    # if not request.user.is_authenticated:
    #     return redirect('sign_in')
    programs = Training_Program.objects.all()
    return render(request, 'home_page.html', {'programs':programs})


def add_training_program(request):
    pass


def edit_training_program(request):
    pass


def delete_training_program(request):
    pass
