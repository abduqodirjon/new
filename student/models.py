from django.db import models

# Create your models here.

class Guruh(models.Model):
    guruh = models.CharField(max_length=80, verbose_name='Guruh')
    def __str__(self) -> str:
        return self.guruh

class Students(models.Model):
    ism = models.CharField(max_length=100, verbose_name="F.I.O")
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.ism

class Results(models.Model):
    guruh = models.ForeignKey(Guruh, on_delete=models.CASCADE)
    natija = models.TextField()

    def __str__(self) -> str:
        return str(self.guruh)