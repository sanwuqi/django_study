from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField("书名", max_length=50, default='')
    price = models.DecimalField('价格', max_digits=7, decimal_places=2)

