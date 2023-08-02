from django.db import models
from django.contrib.auth.models import User as Custom_user


class User(models.Model):
    """
    User model

    name - User's name
    password - User's password
    gender - User's gender
    weight - User's weight
    height - User's height
    email_address - User's email
    """
    user1 = models.OneToOneField(Custom_user, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=70)
    gender = models.CharField(max_length=20, unique=True)
    weight = models.CharField(max_length=100, unique=True)
    height = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=150, unique=True)

    @staticmethod
    def create_user(name, password, gender, weight, height, email):
        """
         Method to create a new user,
         but also checks if user is already exists
         [get user either by mail or by nickname]
        :param name: user's name
        :param password: user's password
        :param gender: user's gender
        :param weight: user's weight
        :param height: user's height
        :param email: user's email
        :return: new user
        """
        user = User(name=name, password=password,gender=gender, weight=weight, height=height, email=email)
        user.save()
        return user

    def add_training_program():
        pass

    def edit_training_program():
        pass
    
    def delete_training_program():
        pass


class Exercise(models.Model):
    """
    Exercise model

    name - Exercise's name
    sets - Exercise's sets amount
    reps - Exercise's reps amount
    """
    name = models.CharField(max_length = 150, unique=True)
    sets = models.IntegerField()
    reps = models.IntegerField()

    def edit_sets():
        pass

    def edit_reps():
        pass


class Training_Program(models.Model):
    """
    Training_Program model

    user_id - FK to User model
    exercises - FK to exercise model
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    excercises = models.ManyToManyField(Exercise)

    def add_exercise():
        pass

    def delete_exercise():
        pass
