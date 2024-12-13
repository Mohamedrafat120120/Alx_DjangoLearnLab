from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView,TemplateView
from .models import post
class register(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('blog/login')
    template_name = 'blog/register.html'
    
class profile(TemplateView):
    template_name = 'blog/profile.html'
    
    
class home(TemplateView):
    template_name = 'blog/home.html'
    
    
class posts(ListView):
    model=post
    template_name = 'blog/posts.html'
    
    
    
class display(ListView):
    model=post
    template_name='blog/display.html'
class display(CreateView):
    model=post
    template_name='blog/display.html'
class display_detail(DetailView):
    model=post
    template_name='blog/display.html'
    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)
    
class update_post(UpdateView):
    model=post
    template_name='blog/display.html'
    fields=['title','content','author']
    success_url=reverse_lazy('display')
    def  form_valid(self, form):
        response=super().form_valid(form)
        return response
    
    
class delete_post(DeleteView):
    model=post
    template_name='blog/delete.html'
    success_url='display'
    