from django.shortcuts import render
from .forms import LoginForms
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
def login_auth(request):
    context = {}
    if request.method == 'POST':
        form = LoginForms(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username = cd['user_name'], password = cd['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Ауэнтификация прошла успешно')
            else:
                return HttpResponse('Аккаунт не активен, простите!')
        else:
            return HttpResponse('Такого логина нет ')
    else:
        form = LoginForms()
        context['form'] = form
    return render (request, 'account/login_form.html', context)

@login_required
def main(request):
    return render(request, 'account/main.html',{'select':'Успешно'})