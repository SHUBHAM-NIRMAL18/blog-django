from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView
from .models import Post

# Using ListView for Listing Blog
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


# Using DetailView for display the Single detailed Blog
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'


#Using CreateView for adding form to add Blog
class BlogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'


#Using UpdateView for editing the Blog
class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']
