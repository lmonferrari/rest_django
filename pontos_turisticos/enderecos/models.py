from django.core.validators import MaxLengthValidator, MinLengthValidator
from django.db import models


class Endereco(models.Model):
    linha1 = models.CharField(max_length=150, null=False, blank=False)
    linha2 = models.CharField(max_length=150)
    cidade = models.CharField(max_length=100, null=False, blank=False)
    estado = models.CharField(max_length=2, null=False, blank=False,
                              validators=[
                                  MinLengthValidator(2),
                                  MaxLengthValidator(2)
                              ])
    pais = models.CharField(max_length=70, null=False, blank=False)
    longitude = models.IntegerField(null=True, blank=True)
    latitude = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.linha1
