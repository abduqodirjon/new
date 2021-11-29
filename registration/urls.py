from django import urls
from django.urls import path
from django.urls import path
from .views import signup, log_in, log_out, edit_profil

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('edit_profil/', edit_profil, name='edit_profil'),
    
]