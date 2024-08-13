from django.urls import path

from tracking.views import dashboard, LeadsListView, OffersListView

app_name = "tracking"

urlpatterns = [
    path("tracking/", dashboard, name="dashboard"),
    path("tracking/leads/", LeadsListView.as_view(), name="leads"),
    path("tracking/offers/", OffersListView.as_view(), name="offers")
]
