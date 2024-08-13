from django.db import models
from django.utils.translation import gettext_lazy as _

from prospector import settings


class Leads(models.Model):
    lead_status = (
        ("", _("Empty")),
        ("invited", _("Invitation/Email sent")),
        ("match", _("Contact initiated")),
        ("call", _("Call planned")),
        ("technical_interview_1", _("Technical Interview Software Firm")),
        ("technical_interview_2", _("Technical Interview final client")),
        ("interview", _("Interview")),
        ("offer", _("Offer")),
        ("ko", _("KO")),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(_("first name"), max_length=150)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = models.EmailField(_("email adress"), blank=True)
    company = models.CharField(_("company"), blank=True, max_length=50)
    status = models.CharField(_("lead status"), choices=lead_status, default="", max_length=50)
    source = models.CharField(_("source"), blank=True, max_length=150)
    date_last_contact = models.DateField(_("Last contact date"))
    date_reminder = models.DateField(_("Next reminder date"))
    status_reminder = models.CharField(_("Reminder status"), max_length=50)


class Offers(models.Model):
    experience = (
        ("0-2", _("0-2 years")),
        ("2-5", _("2-5 years")),
        ("5-10", _("5-10 years")),
    )

    work_rhythm_choices = (
        ("0", _("In person")),
        ("1", _("Hybrid")),
        ("2", _("Full Remote")),
    )

    lead = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=150, blank=False, null=False)
    date_offer = models.DateField(_("Date of offer publication"))
    offer_market = models.CharField(_("Market"), blank=False, max_length=100)
    location = models.CharField(_("Location"), max_length=150)
    experience = models.CharField(_("experience"), choices=experience, max_length=50)
    average_daily_rate = models.IntegerField()
    work_rhythm = models.CharField(_("rhythm"), choices=work_rhythm_choices, max_length=100)
    offer_link = models.URLField()
    activity_area = models.CharField(max_length=100)
    mandatory_technos = models.CharField(max_length=150)
    optional_technos = models.CharField(max_length=150)
    mandatory_skill = models.CharField(max_length=150)
    optional_skill = models.CharField(max_length=150)
    notes = models.TextField()
