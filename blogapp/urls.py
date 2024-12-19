from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),# URL Config for Detail Blog
    path('post/new/', BlogCreateView.as_view(), name='post_new'), #Url Config for blog form
]
