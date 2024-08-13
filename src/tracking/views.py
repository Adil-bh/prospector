from django.shortcuts import render
from django.views.generic import ListView

from tracking.models import Leads, Offers


# Create your views here.


def dashboard(request):
    return render(request, 'dashboard.html')


class LeadsListView(ListView):
    template_name = "leads.html"
    model = Leads

class OffersListView(ListView):
    template_name = "offers.html"
    model = Offers