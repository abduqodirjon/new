from django.urls import path, include
from .views import index, about, natija, statistika, contact
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('course/', natija, name='natija'),
    path('result/', statistika, name='statistika'),
    path('contact/', contact, name='contact'),
    path('news/', include('news.urls')),
]
