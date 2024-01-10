from django import forms

class LoginForms(forms.Form):
    user_name = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 100, widget = forms.PasswordInput)