from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView,ListView,DeleteView,DetailView,UpdateView,TemplateView
from .models import post,Comment
from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseForbidden
from django.contrib.auth.decorators import login_required
from .forms import CustomUserCreationForm,CommentForm
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
    
    
from django.shortcuts import get_object_or_404, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Comment, Post
from .forms import CommentForm

class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/add_comment.html'

    def form_valid(self, form):
        form.instance.author = self.request.user  # Set the comment's author to the logged-in user
        post_id = self.kwargs['post_id']
        form.instance.post = get_object_or_404(Post, id=post_id)  # Link the comment to the associated post
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})  # Redirect to the post detail page


class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'blog/edit_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Allow only the author to edit the comment

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/delete_comment.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Allow only the author to delete the comment

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.id})   