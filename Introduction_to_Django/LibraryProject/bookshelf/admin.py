from django.contrib import admin
from .models import Book
# Register your models here.
class  BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'price')
    list_display_links=('title','author')

admin.site.register(Book)