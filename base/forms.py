from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms
from . models import Profile ,Post ,Comment

class RegisterForm(forms.ModelForm):
    # setting password
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    # second password to confirm 
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    # user model form 
    class Meta:
        model = User
        fields = ['username', 'first_name','last_name', 'email']

    # compare password one and two
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']

    # stops registering with existing email
    # check if the email is unique
    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Email already in use.')
        return data

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)