from django.shortcuts import render
from .forms import LoginForms,UserRegistrationForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

def profile_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)#сохрн. нового поль-ля но не заносим в базу
            new_user.set_password(form.cleaned_data['password'])#присваиваем пол-ль зашифрован пароль
            new_user.save()#созраняем в базу
            return render(request, 'account/register_done.html',{'new_user':new_user})#при успешной регистрации
    else:
        form = UserRegistrationForm()
    return render (request, 'account/register.html', {'form':form})
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