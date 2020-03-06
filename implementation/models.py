from django.db import models

class ImplementationModel(models.Model):
    num1 = models.FloatField(default = '0')
    num2 = models.FloatField(default = '0')
    result = models.FloatField(default = '0')
