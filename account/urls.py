from django.urls import path
from .views import login_auth
from django.contrib.auth import views as auth_view
from .views import main

urlpatterns = [
    # path('', login_auth, name = 'login_auth'),
    path('', auth_view.LoginView.as_view(), name='login'), #обработчик входа
    path('account/logout/', auth_view.LogoutView.as_view(), name='logout'),#обработчик выхода
    path('password_change/',auth_view.PasswordChangeView.as_view(), name= 'password_change'),#пров-т форму смены пароля
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(), name = 'password_change_done'),#возв-т соош-е об успешной отп-ке
    path('password_reset/', auth_view.PasswordResetView.as_view(), name = 'password_reset'),#форма сброса пароля
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(), name = 'password_reset_done'),#воз-ет форму успешной отпавки пароля
    path('password_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),#пров-т отправленную ссылку для вос-ия пароля и возврашает форму заполнения нового пароля
    path('password_reset_complite/', auth_view.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),#ссылка успешной смены пароля

    path('main/',main, name = 'main')

]
