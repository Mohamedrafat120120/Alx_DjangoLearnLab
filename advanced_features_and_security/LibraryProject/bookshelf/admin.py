from django.contrib import admin
from django.contrib.auth.admin import UserAdmin 
from .models import Book,CustomUser
from django.contrib.auth.models import Permission,User,Group
from django.contrib.contenttypes.models import ContentType 
# Register your models here.
new_group,creatd=Group.objects.get_or_create(name='Editors')
contenttype=ContentType.objects.get_for_model(Book)
edit_permission=Permission.objects.get(codename='can_edit_all_books',content_type__app_label='bookshelf',
    content_type__model=contenttype)
add_permission=Permission.objects.get(codename='can_add_book',content_type__app_label='bookshelf',
    content_type__model=contenttype)
new_group.permissions.add(edit_permission,add_permission)

user=User.objects.get(name='micheal')
user.groups.add(user)


user=User.objects.get(name='micheal')
contenttype=ContentType.objects.get(app_label='bookshelf', model='book')
permission=Permission.objects.get(codename='can_view_all_books',contenttype=contenttype)
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