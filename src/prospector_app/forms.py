from django.contrib.auth.forms import UserCreationForm

from prospector_app.models import CustomUser


class CustomSignupForm(UserCreationForm):
    """
        Customisation of the built-in SignupForm in Django by
        changing the user model used from User -> CustomUser
    """
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields
