from django.urls import path, include

from accounts import views, email_activation
from accounts.views import home, signup
from django.contrib.auth import views as auth_views
import django.contrib.auth.urls
app_name = "accounts"

urlpatterns = [
    path("", home, name="home"),
    path("accounts/signup/", signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
    path('activate/<uidb64>/<token>', email_activation.activate, name='activate'),

    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="registration/password_reset.html", email_template_name="registration/password_reset_email.html"), name="reset_password"),
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name="registration/password_reset_done.html"), name="password_reset_done"),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="registration/password_reset_confirm.html"), name="password_reset_confirm"),
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="registration/password_reset_complete.html"), name="password_reset_complete"),

]