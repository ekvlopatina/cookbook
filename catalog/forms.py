from django import forms
from . import models
from django.contrib.auth.models import User

class ReviewForm(forms.ModelForm):
    class Meta:
        model = models.Review
        fields = ("name", "comment")

class UserForm(forms.ModelForm):
    email = forms.CharField(label="E=mail", widget=forms.EmailInput, required=True)
    class Meta:
        model = User
        fields = ('username', 'password', 'email')

class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        fields = ('text', )
