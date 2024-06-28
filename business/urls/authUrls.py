from django.urls import path
from business.views.authView import login_view, register_view, logout_view, recovery_view

urlpatterns = [
    path('login', login_view, name='login'),
    path('register', register_view, name='register'),
    path('logout', logout_view, name='logout'),
    path("recovery", recovery_view, name='recovery'),
]
