from django.db import models

class Nums(models.Model):
    num1 = models.FloatField(default = '0')
    num2 = models.FloatField(default = '0')
    addition = models.FloatField(default = '0')
    subtraction = models.FloatField(default = '0')
    multiplication = models.FloatField(default = '0')
    division = models.FloatField(default = '0')
    userID = models.CharField(max_length = 10)
    date = models.DateTimeField(auto_now_add = True)
    numString = models.CharField(max_length = 10)
    resString = models.CharField(max_length = 1000)

    class Meta:
        db_table = 'nums'
