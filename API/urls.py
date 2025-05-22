from django.urls import path
from . import views

urlpatterns = [
    path("checkin/", views.checkin_view),
    path("checkout/", views.checkout_view),
]
