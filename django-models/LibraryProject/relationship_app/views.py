from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from django.contrib.auth.decorators import user_passes_test
from .models import *
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm 
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.contrib.auth import login 
from django.contrib.auth.decorators import permission_required



# Create your views here.
def list_books(request):
    books=Book.objects.all()
    context={'books':books}
    return render(request,'LibraryProject/templates/relationship_app/list_books.html',context)



class LibraryDetailView(DetailView):
    model = Library
    template_name='LibraryProject/relationship_app/library_detail.html'


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
          
    return render(request,'Alx_DjangoLearnLab/django-models/LibraryProject/relationship_app/User_Authentication/signup.html',{'form':form})

@permission_required('relationship_app.can_add_book',login_url='login/')
def add_book_per(request):
        book=Book.objects.create(title=request.POST['title'],author=request.POST['author'])
@permission_required('relationship_app.can_change_book',login_url='login/')
def change_book_per(request):
        book=get_object_or_404(Book,pk=id)
        book.title=request.POST['title']
        book.author=request.POST['author']
        book.save()
        
        
@permission_required('relationship_app.can_delete_book',login_url='login/')
def delete_book_per(request):
        
        book=get_object_or_404(Book,pk=id)
        book.delete()
        return redirect('list_books')
     


def is_admin(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Admin'

def is_librarian(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Librarian'

def is_member(user):
    return hasattr(user, 'userprofile') and user.userprofile.role == 'Member'

@user_passes_test(is_admin)
def Admin(request):
    return HttpResponse("Welcome, Admin!")

@user_passes_test(is_librarian)
def Librarian(request):
    return HttpResponse("Welcome, Librarian!")

@user_passes_test(is_member)
def Member(request):
    return HttpResponse("Welcome, Member!")    