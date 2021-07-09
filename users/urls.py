from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns = [
    path('registro', registro, name='registro'),
    path('login', auth_views.LoginView.as_view(template_name='users/login.html')),
    path('logout', logout_view, name='logout_view'),
]
