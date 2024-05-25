from django.contrib import admin

from django.contrib.admin.decorators import register
from .models import Book
# Register your models here.
@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['name','price','authorName']
