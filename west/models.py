from django.db import models
from django import forms


# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name


class CharacterForm(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField(max_value=200)
