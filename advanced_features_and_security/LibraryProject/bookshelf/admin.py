from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Book,user
# Register your models here.
class CustomUserAdmin(UserAdmin):
    
    model = user
    list_display = [
        'email', 'username', 'date_of_birth'
    ]
class  BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links=('title','author')
    list_filter=['publication_year']
    search_fields=['title']

admin.site.register(Book,BookAdmin)
admin.site.register(user,CustomUserAdmin)