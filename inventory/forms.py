from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Vendor, Product, Comment, Rating

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class VendorForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        exclude = ['user']

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        widgets = {
            'image': forms.ClearableFileInput(attrs={'multiple': False}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating']

class NotificationPreferenceForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['notification_preferences']

class ReviewIntervalForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['review_interval_days']
        widgets = {
            'review_interval_days': forms.NumberInput(attrs={'min': 1}),
        }
