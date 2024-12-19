from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Using ListView for Listing Posts
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'


# Using DetailView for display the Single detailed Post
class BlogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'
    