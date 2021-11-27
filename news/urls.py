from django.urls import path
from . import views

urlpatterns = [
    path('', views.yangilik, name='yangilik'),
    path('add/', views.yan_add, name="yan_add"),
    path('add_test/', views.yan_add_test, name="yan_add_test"),
    path('<int:pk>/edit', views.edit, name="edit"),
    path('<int:pk>/delete', views.delete, name="delete"),
]
