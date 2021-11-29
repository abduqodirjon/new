from django.urls import path
from . import views

urlpatterns = [
    path('', views.yangilik, name='yangilik'),
    path('add/', views.yan_add, name="yan_add"),
    path('<str:pk>/edit', views.edit, name="yan_edit"),
    path('<str:pk>/delete', views.delete, name="yan_delete"),
]
