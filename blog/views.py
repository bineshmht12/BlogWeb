from django.urls import reverse_lazy
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView

from .models import Post


class BlogListView(ListView):
    model = Post
    template_name ='blog/home.html'
    context_object_name = 'object_list'
    
    
class DetailViewPage(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name ='individual_post'
    
    
    
class BlogCreateView(CreateView):
    template_name = 'blog/post_new.html'
    model = Post
            
    fields = ['title', 'author', 'content']
    
    
            
    
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'blog/post_edit.html'
    fields = ['title', 'content']
    
class BlogDeleteView(DeleteView):
    model = Post
    template_name='blog/post_delete.html'
    success_url = reverse_lazy('blog:home')