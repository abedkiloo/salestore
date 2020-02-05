from django.db import models


# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=255)
    # description = models.CharField(max_length=255)
    stock = models.IntegerField()
    price = models.FloatField()
    image_url = models.CharField(max_length=3000)


class Offer(models.Model):
    code = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    discount = models.FloatField()
