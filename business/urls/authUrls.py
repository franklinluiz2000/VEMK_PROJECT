from django.urls import path
from business.views.authView import login_view

urlpatterns = [
    path('login', login_view, name='login')
]
