from django.db import models
from django.db.models.fields import CharField
from ckeditor.fields import RichTextField
# Create your models here.

class Category(models.Model):
    category = CharField(max_length=150)

    def __str__(self) -> str:
        return self.category

class News(models.Model):
    title = models.CharField(max_length=200, verbose_name="Sarlavha", unique=False)
    body = models.CharField(max_length=250,verbose_name="Mazmuni")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Kategoriyasi")
    image = models.ImageField(upload_to='news_img', blank=True, null=True, verbose_name="Rasm")
    text_full = RichTextField(verbose_name="To\'liq matni")
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.title