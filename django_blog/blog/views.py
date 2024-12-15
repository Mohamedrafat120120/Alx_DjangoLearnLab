from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView,TemplateView
from .models import post
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

@login_required
def profile(request):
    if request.method == 'POST':
        user = request.user
        user.email = request.POST.get('email', user.email)
        user.save()
        return redirect('profile')
    return render(request, 'blog/profile.html', {'user': request.user})

    
    
class home(TemplateView):
    template_name = 'blog/home.html'
    
    
class posts(ListView):
    model=post
    template_name = 'blog/posts.html'
    queryset=post.objects.all()
    context_object_name='post'
    
    
    
class display(ListView):
    model=post
    template_name='blog/listing.html'
    queryset=post.objects.all()
    context_object_name='post'
    
    
class display_create(CreateView):
    model=post
    template_name='blog/creating.html'
    fields = ['title', 'content', 'author']
    success_url = reverse_lazy('listing')
class display_detail(DetailView):
    model=post
    template_name='blog/viewing.html'
    context_object_name='post'
    
   
    
class update_post(UpdateView):
    model=post
    template_name='blog/editing.html'
    fields=['title','content','author']
    success_url=reverse_lazy('listing')
    def  form_valid(self, form):
        response=super().form_valid(form)
        return response
    
    
class delete_post(DeleteView):
    model=post
    template_name='blog/deleting.html'
    success_url='listing'
    