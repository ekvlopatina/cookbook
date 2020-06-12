from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Dish(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    photo = models.ImageField(upload_to='', null=True, blank=True)
    ingredients = models.TextField(max_length=1000)
    calorie = models.IntegerField()
    recipe = models.TextField(max_length=1500)

    def __str__(self):
        return self.name
