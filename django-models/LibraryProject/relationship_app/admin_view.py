from .models import UserProfile
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test


def is_admin(user):
    return UserProfile.User=='Admin'

@user_passes_test(is_admin)
def admin(request):
    return render(request,'admin.html')