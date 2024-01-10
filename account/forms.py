from django import forms
from django.contrib.auth.models import User

class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','email']
    password = forms.CharField(max_length = 100, label= 'password', widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=100, label='repeat', widget=forms.PasswordInput)

    def clean_password2(self):
        cd  = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('пароли не совпадают')
        return cd['password2']

'''Метод clean_password2 проверяет корректность поля  password2.
т.е. в нашем случае совпадение с password, добавляя clean_ к названию поля формы , можно проверять кореректность 
поля
'''


class LoginForms(forms.Form):
    user_name = forms.CharField(max_length = 100)
    password = forms.CharField(max_length = 100, widget = forms.PasswordInput)