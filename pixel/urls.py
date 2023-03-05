from django.urls import path
from .views import LeadView, LeadDarkView, re_dark, re_white

urlpatterns = [
    path('', LeadView.as_view(), name='index'),
    path('dark/', LeadDarkView.as_view(), ),
    path('re_dark', re_dark, ),
    path('re_white', re_white, ),
]