from django.urls import path, include
from prospector_app.views import home, signup
import django.contrib.auth.urls
app_name = "prospector"

urlpatterns = [
    path("", home, name="home"),
    path("accounts/signup/", signup, name="signup"),
    path("accounts/", include("django.contrib.auth.urls")),
]