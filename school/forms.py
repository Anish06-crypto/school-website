from typing import Pattern
from django import forms
from django.db.models import fields
from .models import News

class NewsAddForm(forms.ModelForm):
    class Meta:
        model = News
        fields = "__all__"

class CareerForm(forms.Form):

        Name = forms.CharField(max_length = 50)
        Email = forms.EmailField(max_length = 150)
        Mobile_Number = forms.CharField(min_length=10, max_length = 10)
        Place = forms.CharField(max_length=50)
        Department = forms.CharField(max_length=50)
        Position_Applying_for = forms.CharField(max_length=50)
