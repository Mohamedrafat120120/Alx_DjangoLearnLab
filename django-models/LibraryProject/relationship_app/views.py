from django.shortcuts import render
from .models import Book,Library
from django.views.generic import ListView
# Create your views here.
def list_all_books(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request,'templates/relationship_app/list_books.html',context)



class list_books(ListView):
    model = Library
    template_name='relationship_app/library_detail.html'
