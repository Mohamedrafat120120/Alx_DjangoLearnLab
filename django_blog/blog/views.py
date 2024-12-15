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
    
    
@login_required
def add_comment(request, post_id):
    post = get_object_or_404(post, id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author = request.user
            comment.save()
            return redirect('post_detail', pk=post.id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})

@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('post_detail', pk=comment.post.id)
    else:
        form = CommentForm(instance=comment)
    return render(request, 'blog/edit_comment.html', {'form': form, 'comment': comment})

@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.author:
        return HttpResponseForbidden()
    post_id = comment.post.id
    comment.delete()
    return redirect('post_detail', pk=post_id)    