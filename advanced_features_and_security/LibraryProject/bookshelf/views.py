from django.shortcuts import render
from .models import Book
from django.contrib.auth.decorators import permission_required
from .forms import ExampleForm
# Create your views here.
@permission_required('bookshelf.can_edit',raise_exception=True)
def edit(request):
    book_list=Book.objects.all()
    return render(request,'bookshelf/edit.html',{'book_list':book_list})


def form(request):
    
    return render(request,'bookshelf/form_example.html',{'lf':ExampleForm})
    
