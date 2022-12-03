from django.db import models

# Create your models here.

class City(models.Model):
    name = models.CharField(max_length=35)
    countrycode = models.CharField(max_length=3)

    def __str__(self):
        return self.name
