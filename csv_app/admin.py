from django import forms
from django.contrib import admin

from .models import ColumnSet, Column, Type

# Register your models here.


admin.site.register(Column)
admin.site.register( Type)
admin.site.register(ColumnSet)
