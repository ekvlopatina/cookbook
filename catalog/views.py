from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, get_object_or_404

from catalog.models import Category, Dish
from . import forms
from .models import Comment, Bookmark

def index(request):
    num_dish = Dish.objects.count()
    dish_main_courses = Category.objects.get(name="Вторые блюда").dish_set.all()[0:2]
    dish_salads = Category.objects.get(name="Салаты").dish_set.all()[0:2]
    dish_desserts = Category.objects.get(name="Десерты").dish_set.all()[0:2]
    context = {
        'num_dish': num_dish,
        'dish_main_courses': dish_main_courses,
        'dish_salads': dish_salads,
        'dish_desserts': dish_desserts,
    } 
    return render(request, 'index.html', context=context)

# class SaladsView(generic.ListView):
#     model = Dish
#
# class DessertsView(generic.ListView):
#     model = Dish
#
# class MainCoursesView(generic.ListView):
#     model = Dish

def salads(request):
    dish_list = Dish.objects.filter(category__name='Салаты')
    context = {
    'dish_list': dish_list,
    }
    return render(request, 'catalog/dish_salads.html', context=context)

def desserts(request):
    dish_list = Dish.objects.filter(category__name='Десерты')
    context = {
    'dish_list': dish_list,
    }
    return render(request, 'catalog/dish_desserts.html', context=context)

def main_courses(request):
    dish_list = Dish.objects.filter(category__name='Вторые блюда')
    context = {
    'dish_list': dish_list,
    }
    return render(request, 'catalog/dish_main_courses.html', context=context)

def dish(request):
    if request.method == "POST":
        if "bookmark_submit" in request.POST:
            new_bookmark = Bookmark.objects.create(user=request.user, dish=Dish.objects.get(id=request.GET.get("id")))
            new_bookmark.save()
        else:
            comment_form = forms.CommentForm(request.POST)
            new_comment = comment_form.save(commit=False)
            new_comment.user = request.user
            new_comment.dish = Dish.objects.get(id=request.GET.get("id"))
            new_comment.save()
        return HttpResponseRedirect(("{}?id=" + request.GET.get("id") + "").format(reverse('dish', kwargs={})))
    else:
        comment_form = forms.CommentForm()
        curr_dish=get_object_or_404(Dish.objects, id=request.GET.get("id"))
        user_comments = Comment.objects.filter(dish__id=request.GET.get("id"))
        dish_in_bookmarks = None
        if request.user.is_authenticated:
            search = request.user.bookmark.filter(dish=curr_dish)
            if search:
                dish_in_bookmarks = True
        context = {
        "curr_dish": curr_dish,
        "comment_form": comment_form,
        "user_comments": user_comments,
        "dish_in_bookmarks": dish_in_bookmarks,
        }
        return render(request, 'catalog/dish.html', context=context)

def about(request):
    if request.method == "POST":
        review_form = forms.ReviewForm(request.POST)
        review_form.save()
        return HttpResponseRedirect('{}?sent=True'.format(reverse('about', kwargs={})))
    else:
        review_form = forms.ReviewForm()
        context={
        'review_form' : review_form,
        'sent': request.GET.get('sent', False)
        }
        return render(request, 'catalog/about.html', context=context)
def signup(request):
    if request.method == "POST":
        user_form = forms.UserForm(request.POST)
        if user_form.is_valid():
            User.objects.create_user(user_form.cleaned_data['username'],
                                    user_form.cleaned_data['email'],
                                    user_form.cleaned_data['password'])
            user = authenticate(
                username=user_form.cleaned_data['username'],
                password=user_form.cleaned_data['password']
            )
            if user is not None:
                login(request, user)
            else:
                print('User login failed')
            return redirect('/')
    else:
        user_form = forms.UserForm()
        context = {
            'user_form': user_form,
        }
        return render(request, 'registration/signup.html', context=context)
from django.contrib.auth.decorators import login_required
@login_required(login_url="login")
def profile(request):
    if request.method == "POST":
        Bookmark.objects.get(id=request.POST.get("delete-bookmark")).delete()
        return redirect('profile')
    else:
        bookmarks = request.user.bookmark.all()
        comments = request.user.comment.all()
        context = {
            "bookmarks": bookmarks,
            "comments": comments,
        }
        return render(request, 'catalog/profile.html', context=context)
