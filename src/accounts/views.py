from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.translation import gettext_lazy as _

from accounts.forms import CustomSignupForm
from accounts.models import CustomUser
from accounts.token import account_activation_token


# Create your views here.
def home(request):
    return render(request, "home.html")


# User account creation
def activate(request, uidb64, token):
    '''
    Function that activates user account when email link has been clicked on. Then redirects the user on an
    other page.
    '''
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Merci d'avoir confirmé votre email. Vous pouvez maintenant vous connecter. ")
        return redirect("accounts:login")

    messages.error(request, "Lien d'activation invalide.")
    return redirect('accounts:home')


def activateEmail(request, user, to_email):
    '''
    Function that send confirmation email to user.
    '''
    mail_subject = _("Activez votre compte")
    message = render_to_string("activate_account/template_activate_account.html", {
        'user': user.username,
        'domain': get_current_site(request).domain,
        'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        'token': account_activation_token.make_token(user),
        'protocol': 'https' if request.is_secure() else 'http'
    })
    email = EmailMessage(mail_subject, message, to=[to_email])
    if email.send():
        messages.success(request, f"Cher {user}, veuillez vérifier votre adresse email {to_email}")
    else:
        messages.error(request, f"Problem sending email to {to_email}, check if you typed it correctly.")


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
