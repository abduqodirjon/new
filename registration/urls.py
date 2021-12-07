from django import urls
from django.urls import path
from django.urls import path
from .views import signup, log_in, log_out, edit_profil, user_detail

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', log_in, name='login'),
    path('logout/', log_out, name='logout'),
    path('user_detail/', user_detail, name='user_detail'),
    path('edit_profil/', edit_profil, name='edit_profil'),
    
]