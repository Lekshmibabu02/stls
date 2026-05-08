from django.urls import path
from .views import TrafficSignalActionView

urlpatterns = [
    path('calculate-action/', TrafficSignalActionView.as_view(), name='calculate-action'),
]
