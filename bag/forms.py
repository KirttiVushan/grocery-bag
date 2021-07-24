from django.forms import ModelForm, fields
from .models import Groceries
from django import forms

class Groceries_list(forms.ModelForm):
    class Meta:
        model=Groceries
        fields=['name', 'quantity', 'status','date']




    