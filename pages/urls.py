from django.urls import path, include
from .views import index, about, natija, statistika, contact, admin_panel, add_teacher
urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('course/', natija, name='natija'),
    path('result/', statistika, name='statistika'),
    path('contact/', contact, name='contact'),
    path('news/', include('news.urls')),
    path('admin_panel/', admin_panel),
    path('add_teacher/', add_teacher, name='add_teacher'),
]
