from django.db import models

# Create your models here.
class Moshina(models.Model):
    yili = models.IntegerField(default=2020)
    narxi = models.IntegerField(default=1)
    turi = models.CharField(max_length=24)
    rangi = models.CharField(max_length=25)
    rasmcha = models.CharField(max_length=1000)


    def __str__(self):
        return f"{self.yili} {self.narxi} {self.turi} {self.rangi}"