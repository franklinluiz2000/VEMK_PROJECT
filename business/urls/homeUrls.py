from django.urls import path
from business.views.homeView import home_view

urlpatterns = [
    path("", home_view)
]
