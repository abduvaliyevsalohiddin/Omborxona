from django.db import models
from accounts.models import Ombor
from asosiy.models import Mahsulot, Mijoz


class Statistika(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.SET_NULL, null=True)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.SET_NULL, null=True)
    miqdor = models.PositiveSmallIntegerField(default=1)
    summa = models.PositiveSmallIntegerField()
    tolangan_summa = models.PositiveSmallIntegerField()
    sana = models.DateField(null=True, auto_now_add=True)
    nasiya = models.PositiveSmallIntegerField(default=0)
    ombor = models.ForeignKey(Ombor, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"{self.mahsulot} --> {self.mijoz}"
