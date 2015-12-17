from django.db import models
from django import forms
from django.contrib import admin

# Create your models here.

class Character(models.Model):
    name = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Contact(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=0)
    email = models.EmailField()
    def __str__(self):
        return self.name

class Tag(models.Model):
    contact = models.ForeignKey(Contact)
    name = models.IntegerField(default=0)
    def __str__(self):
        return self.name

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    inlines = [TagInline]
    fieldsets = (
        ['Main',
         {'fields':('name','email')}],

        ['Advance',{
            'classes':('collapse',),
            'fields':('age',)}
        ]
    )

    list_display = ('name','age', 'email')
    search_fields =('name','age')

class CharacterForm(forms.Form):
    name = forms.CharField(max_length=200)
    age = forms.IntegerField(max_value=200)
