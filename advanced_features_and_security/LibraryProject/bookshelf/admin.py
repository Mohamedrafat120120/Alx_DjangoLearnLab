from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Book,CustomUser
from django.contrib.auth.models import Permission,User
from django.contrib.contenttypes.models import ContentType 
# Register your models here.
permission=Permission.objects.get('bookshelf.can_view_all_books')
user=User.objects.get(name='micheal')
contenttype=ContentType(Book)
user.user_permissions.add(permission)

class CustomUserAdmin(UserAdmin):
    
    model = CustomUser
    list_display = [
        'email', 'username', 'date_of_birth'
    ]
class  BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')
    list_display_links=('title','author')
    list_filter=['publication_year']
    search_fields=['title']

admin.site.register(Book,BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)