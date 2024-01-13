from django.urls import path
from .views import login_auth
from django.contrib.auth import views as auth_view
from .views import main, profile_register,edit
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', login_auth, name = 'login_auth'),
    path('main/', main, name='main'),

    path('account/login/', auth_view.LoginView.as_view(), name='login'), #обработчик входа
    path('account/logout/', auth_view.LogoutView.as_view(), name='logout'),#обработчик выхода
    path('password_change/',auth_view.PasswordChangeView.as_view(), name= 'password_change'),#пров-т форму смены пароля
    path('password_change/done/',auth_view.PasswordChangeDoneView.as_view(), name = 'password_change_done'),#возв-т соош-е об успешной отп-ке
    path('password_reset/', auth_view.PasswordResetView.as_view(), name = 'password_reset'),#форма сброса пароля
    path('password_reset_done/',auth_view.PasswordResetDoneView.as_view(), name = 'password_reset_done'),#воз-ет форму успешной отпавки пароля
    path('password_confirm/<uidb64>/<token>/',auth_view.PasswordResetConfirmView.as_view(), name = 'password_reset_confirm'),#пров-т отправленную ссылку для вос-ия пароля и возврашает форму заполнения нового пароля
    path('password_reset_complite/', auth_view.PasswordResetCompleteView.as_view(), name = 'password_reset_complete'),#ссылка успешной смены пароля
    path('register/',profile_register, name = 'register' ),
    path('account/edit/',edit, name = 'edit'),

]


if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

