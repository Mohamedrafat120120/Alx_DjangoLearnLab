from django.shortcuts import render

# Create your views here.

def index(request):
    if user.has_perm('bookshelf.can_edit_all_books'):
        return render(request, 'bookshelf/index.html')
