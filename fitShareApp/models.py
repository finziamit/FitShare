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
    
    @staticmethod
    def get_user_by_email(email):
        """
        Method get email and return User object if exist, otherwise None
        :param email: the user's email
        :return: User object
        """
        user = User.objects.get(email=email)
        return user
    
    @staticmethod
    def delete_user_by_email(email):
        """
         Method to delete a user by his email
        :param email: email to get the user
        :return:  TRUE/FALSE if the user deleted/not
        """
        user = User.get_user_by_nickname(email=email)
        if user not in User.objects.all():
            raise User.DoesNotExist
        else:
            user.delete()


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

    def __str__(self):
        return f"{self.__name}\t{self.__reps}x{self.__sets}"
    
    def edit_exercise(self, sets, reps):
        if sets > 0:
            self.__sets = sets
        if reps > 0:
            self.__reps = reps
        self.save()


class Training_Program(models.Model):
    """
    Training_Program model

    user_id - FK to User model
    exercises - FK to exercise model
    """
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    excercises = models.ManyToManyField(Exercise)

    def __str__(self):
        return f"{self.__user_id}'s Training program"
