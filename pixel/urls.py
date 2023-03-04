from django.urls import path
from .views import LeadView

urlpatterns = [
    path('', LeadView.as_view(), name='index'),
]