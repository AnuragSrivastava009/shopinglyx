

from django.contrib import admin
from django.urls import path,include
from app import views as dash_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
    path('register/',dash_views.register,name='register'),
    path('login/',auth_views.LoginView.as_view(template_name="app/login.html"),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name="app/logout.html",),name='logout'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name="app/passwordchange.html",success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeDoneView.as_view(template_name="app/passwordchangedone.html"),name='passwordchangedone'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name="app/password_reset.html"),name='passwordreset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name="app/password_reset_done.html"),name='passwordresetdone'),
    path('password_reset_confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="app/password_reset_confirm.html"),name='passwordresetconfirm'),
    path('password-reset-complete',auth_views.PasswordResetCompleteView.as_view(template_name="app/password_reset_complite.html"),name='passwordresetcomplete'),
]         
