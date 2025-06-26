
from django.db import models

class Flavor(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    season = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    ingredients = models.ManyToManyField('Ingredient')

    def __str__(self):
        return self.name

class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)
    quantity = models.IntegerField()
    unit = models.CharField(max_length=20)
    is_allergen = models.BooleanField(default=False)

    def __str__(self):
        return self.name

# cafe/models.py

from django.contrib.auth.models import User

class Suggestion(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.TextField()
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Allergen(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class UserAllergy(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    allergen = models.ForeignKey(Allergen, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    flavor = models.ForeignKey(Flavor, on_delete=models.CASCADE)

class CustomUser(models.Model):
    email = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.email
