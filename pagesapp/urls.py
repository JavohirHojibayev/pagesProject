from django.urls import path
from django.urls import path
from .views import AboutPageView  # Correct the view import name

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),  # Use the correct view name
    # Other URL patterns if any
]
