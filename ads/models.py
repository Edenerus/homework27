from django.db import models


class Categories(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Ads(models.Model):
    STATUS = [
        ("TRUE", "Опубликовано"),
        ("FALSE", "Не опубликовано"),
    ]
    name = models.CharField(max_length=150)
    author = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    address = models.CharField(max_length=200)
    is_published = models.CharField(max_length=6, choices=STATUS, default="FALSE")
