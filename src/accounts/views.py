from django.shortcuts import render, redirect

from accounts.email_activation import activateEmail
from accounts.forms import CustomSignupForm


# Create your views here.
def home(request):
    return render(request, "home.html")


def signup(request):
    context = {}
    if request.method == "POST":
        form = CustomSignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            activateEmail(request, user, form.cleaned_data.get('email'))
            return redirect("accounts:login")
        else:
            context["errors"] = form.errors

    form = CustomSignupForm()
    context["form"] = form

    return render(request, "accounts/signup.html", context=context)
