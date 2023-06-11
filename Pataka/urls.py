from django.urls import path
from .views import Pataka, about,contact

urlpatterns = [
    path("", view=Pataka, name='Pataka' ),
    path("about", view=about, name='about'),
    path("contact", view=contact, name="contact")
]