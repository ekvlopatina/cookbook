from django.contrib import admin
from .models import Category, Dish, Review, Comment, Bookmark
# Register your models here.
admin.site.register(Category)
admin.site.register(Dish)
admin.site.register(Review)
admin.site.register(Comment)
admin.site.register(Bookmark)
