from django.db import models
from django.contrib.auth.models import User

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

class Review(models.Model):
    name = models.CharField("Ваше имя", max_length=200)
    comment = models.TextField('Комментарий')
    date = models.DateTimeField("Дата", auto_now_add=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"

    def __str__(self):
        return "Отзыв № " + str(self.id) + " от " + self.date.strftime('%Y-%m-%d %H:%M')

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comment", null=True)
    date = models.DateTimeField("Дата", auto_now_add=True)
    text = models.TextField("Текст")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="comment")

    def __str__(self):
        return str(self.user) + ". Коммент. на блюдо " + str(self.dish)\
         + ", " + str(self.date.strftime('%Y-%m-%d %H:%M')) + ": " + str(self.text)

    class Meta:
        ordering = ['-date']
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"

class Bookmark(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookmark")
    dish = models.ForeignKey(Dish, on_delete=models.CASCADE, related_name="bookmark")

    def __str__(self):
        return str(self.user) + ". Закладка на " + str(self.dish)

        class Meta:
            verbose_name = "Закладка"
            verbose_name_plural = "Закладки"
    
