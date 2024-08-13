from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return "user_{0}/{1}".format(instance.user.id, filename)


class CustomUser(AbstractUser):
    email = models.EmailField(_("email address"), unique=True, blank=True)
    curriculum_vitae = models.FileField(_("resume"), upload_to=user_directory_path)
    linkedin_link = models.URLField(_("linkedin link"), max_length=200)
    prospection_email = models.EmailField(_("email address for prospection"), blank=True)
    prospection_password = models.CharField(_("prospection password"), max_length=128, blank=True)

    @staticmethod
    def get_absolute_url():
        return reverse('accounts:home')
