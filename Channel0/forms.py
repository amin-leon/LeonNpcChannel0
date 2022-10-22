from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import *


class IssueForm(forms.ModelForm):
    class Meta:
        model = Issue
        fields = ['student_id', 'leader_id', 'issue_desc', 'sub_date', 'status']


class AnnouncementForm(forms.ModelForm):
    class Meta:
        model = Annoucement
        fields = '__all__'


class ResponseForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = '__all__'


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = Leader
        fields = ('first_name', 'middle_name', 'last_name', 'sex', 'profile_pic', 'police_number', 'rank', 'telephone',
                  'position', 'registration_date', 'email', 'password1', 'password2')
