from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Answer

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=["username","email",
                "password1","password2"]

class UserUpdateForm(forms.ModelForm):
    email=forms.EmailField()

    class Meta:
        model=User
        fields=['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:

        model=Profile
        fields=['image','bio', "skills",
            'github','linkedin']

class AnswerForm(forms.ModelForm):
    class Meta:
        model=Answer
        fields=['answer_field']
