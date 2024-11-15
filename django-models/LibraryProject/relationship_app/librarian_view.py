from .models import UserProfile
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import user_passes_test


def is_librarian(user):
    return UserProfile.User=='Librarian'

@user_passes_test(is_librarian)
def librarian(request):
    return render(request,'librarian.html')