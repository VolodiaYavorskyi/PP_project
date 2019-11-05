from django.db import models


class Drug(models.Model):
    name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


class Order(models.Model):
    drugName = models.CharField(max_length=30)
    quantity = models.IntegerField()


class Demand(models.Model):
    drugName = models.CharField(max_length=30)

    def __str__(self):
        return self.drugName
