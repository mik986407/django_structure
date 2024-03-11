from django import forms
from django.db import models

class MyForm(forms.Form):
    my_image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class YourModel(models.Model):
    image = models.ImageField(upload_to='images/')