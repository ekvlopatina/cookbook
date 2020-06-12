from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salads', views.SaladsView.as_view(template_name_suffix="_salads"), name='salads'),
    path('dessert', views.DessertsView.as_view(template_name_suffix="_desserts"), name='desserts'),
    path('main_course', views.MainCoursesView.as_view(template_name_suffix="_main_courses"), name='main_courses'),
]
