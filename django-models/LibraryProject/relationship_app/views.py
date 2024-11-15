from django.shortcuts import render
from .models import Book
from .models import Library
from django.views.generic.list import ListView
# Create your views here.
def list_all_books(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request,'templates/relationship_app/list_books.html',context)



class list_books(ListView):
    model = Library
    template_name='relationship_app/library_detail.html'
