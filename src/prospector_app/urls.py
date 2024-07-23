from django.urls import path
from prospector_app.views import home

app_name = "prospector_app"

urlpatterns = [
    path("", home, name="home")
]