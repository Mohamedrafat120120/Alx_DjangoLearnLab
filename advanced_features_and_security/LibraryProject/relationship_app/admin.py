from django.contrib import admin
from .models import *
from django.contrib.auth.models import User,Permission
from django.contrib.contenttypes.models import ContentType
# Register your models here.
# user=User.objects.get(username='hamoda')
# content_type=ContentType.objects.get_for_model(Book)
# permission=Permission.objects.get(codename="can_add_book",content_type=content_type)
# user.user_permissions.add(permission)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(UserProfile)
admin.site.register(Librarian)
admin.site.register(Library)
