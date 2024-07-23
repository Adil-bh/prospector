from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import render

from prospector_app.forms import CustomSignupForm
from prospector_app.models import CustomUser


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    context = {}

    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Bienvenue !")
        else:
            context["errors"] = form.errors

    form = CustomSignupForm()
    context["form"] = form

    return render(request, "accounts/signup.html", context=context)
