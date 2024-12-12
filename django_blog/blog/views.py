from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView
from .models import post
class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'blog/register.html'
    
    
class display(ListView):
    model=post
    template_name='blog/display.html'
class display(CreateView):
    model=post
    template_name='blog/display.html'
class display(DetailView):
    model=post
    template_name='blog/display.html'
class display(UpdateView):
    model=post
    template_name='blog/display.html'
class display(DeleteView):
    model=post
    template_name='blog/display.html'
    