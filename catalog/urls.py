from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('salad', views.salads, name='salads'),
    path('main_course', views.main_courses, name='main_courses'),
    path('dessert', views.desserts, name='desserts'),
    path('about', views.about, name='about'),
    path('dish', views.dish, name='dish'),
    path('profile', views.profile, name='profile'),
]
# urlpatterns = [
#     path('', views.index, name='index'),
#     path('salad', views.SaladsView.as_view(template_name_suffix="_salads"), name='salads'),
#     path('dessert', views.DessertsView.as_view(template_name_suffix="_desserts"), name='desserts'),
#     path('main_course', views.MainCoursesView.as_view(template_name_suffix="_main_courses"), name='main_courses'),
# ]
