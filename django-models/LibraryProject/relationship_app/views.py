from django.shortcuts import render,redirect
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login 
# Create your views here.
def list_books(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request,'templates/relationship_app/list_books.html',context)



class LibraryDetailView(DetailView):
    model = Library
    template_name='library_detail.html'


# class registeration(CreateView):
#     form_class = UserCreationForm
#     success_url=reverse_lazy('login')
#     template_name='relationship_app/signup.html'


def register(request):
    if request.method=='POST':
      form=UserCreationForm(request.POST)
      if form.is_valid():
          form.save()
          return redirect('login')
      else:
          form=UserCreationForm()
          
    return render(request,'templates/relationship_app/user_authentication/signup.html',{'form':form})
