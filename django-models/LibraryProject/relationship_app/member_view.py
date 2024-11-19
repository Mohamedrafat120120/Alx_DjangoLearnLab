from .models import UserProfile
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test


def is_member(user):
    return UserProfile.User=='Member'

@user_passes_test(is_member)
def member(request):
    return render(request,'member.html')