from django.shortcuts import render
from .forms import LoginForms,UserRegistrationForm, UserEditForm, ProfileEditForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Profile
from django.contrib.auth.models import User

@login_required
def edit(request):
    if request.method == 'POST':
        user_form = UserEditForm(instance=request.user, data = request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,data =  request.POST, files = request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
    else:
        # user_post = User.objects.get(user = request.user)
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)
    return render(request, 'account/edit.html',{'user_form':user_form,'profile_form':profile_form})

def profile_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)#сохрн. нового поль-ля но не заносим в базу
            new_user.set_password(form.cleaned_data['password'])#присваиваем пол-ль зашифрован пароль
            new_user.save()#сохраняем в базу
            Profile.objects.create(user = new_user)
            return render(request, 'account/register_done.html',{'new_user':new_user,})#при успешной регистрации
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
    return render(request, 'account/main.html',{'select':'Это текст главной страницы'})