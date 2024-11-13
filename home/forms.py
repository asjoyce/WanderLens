from django import forms

class TripPlanForm(forms.Form):
    days = forms.IntegerField(label='Number of Days', min_value=2, max_value=10, widget=forms.NumberInput(attrs={'id': 'days'}))
    budget = forms.ChoiceField(label='Budget', choices=[], required=False, widget=forms.Select(attrs={'id': 'budget'}))
    people = forms.IntegerField(label='Number of People', min_value=1, widget=forms.NumberInput(attrs={'id': 'people'}))

# forms.py
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)
