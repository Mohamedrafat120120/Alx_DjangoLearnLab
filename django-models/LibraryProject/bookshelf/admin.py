from django.contrib import admin
from .models import Book
# Register your models here.
class  BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links=('title','author')
    list_filter=['publication_year']
    search_fields=['title']

admin.site.register(Book,BookAdmin)