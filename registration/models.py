from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image
from .decorators import unauthenticated_user
# Create your models here.
  

class CustomUser(AbstractUser):
    u_fio = models.CharField(max_length=150, verbose_name="O\'quvchi F.I.O", blank=True, null=True)
    guruhi = models.CharField(max_length=20, verbose_name="Guruhi", blank=True, null=True)
    m_fio = models.CharField(max_length=150, verbose_name="Ma\'sul F.I.O")
    tel = models.CharField(max_length=25, verbose_name="Telefon raqam")
    manzil = models.CharField(max_length=200, verbose_name="Manzil" , blank=True, null=True)
    image = models.ImageField(upload_to='users_img', blank=True, null=True, verbose_name="Rasm:")




 