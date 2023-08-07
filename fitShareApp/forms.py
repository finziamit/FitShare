from django import forms
from .models import Training_Program, Exercise, User
from django.contrib.auth.models import User as Custom_user


class AddTrainingProgramForm(forms.ModelForm):
    class Meta:
        model = Training_Program
        fields = ('user_id', 'excercises')
        widgets = {'user_id': forms.HiddenInput()}


class NewUserForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
            attrs={'class': 'form-control', 'placeholder': 'example@example.com'}))
    name = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Name'}))
    password = forms.CharField(required=True, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Password'}))
    password_confirm = forms.CharField(required=True, widget=forms.PasswordInput(
            attrs={'class': 'form-control', 'placeholder': 'Confirm Password'}))
    gender = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Gender'}))
    weight = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Weight'}))
    height = forms.CharField(required=True, widget=forms.TextInput(
            attrs={'class': 'form-control', 'placeholder': 'Height'}))
    
    class Meta:
        model = User
        fields = ('name', 'password', 'gender', 'weight', 'height', 'email')

        def clean(self):
            cleaned_data = super().clean()
            password = cleaned_data.get("password")
            password_confirm = cleaned_data.get("password_confirm")

            if password != password_confirm:
                raise forms.ValidationError("Passwords do not match")


class EditTrainingProgramForm(forms.ModelForm):
    class Meta:
        model = Training_Program
        fields = ('excercises',)


class UserForm(forms.ModelForm):
    class Meta:
        model = Custom_user
        fields = ('password', 'email')


class CustomUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('name',)
