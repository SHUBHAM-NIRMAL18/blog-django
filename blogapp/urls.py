from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('post/<int:pk>/', BlogDetailView.as_view(), name='post_detail'),# URL Config for Detail Blog
    path('post/new/', BlogCreateView.as_view(), name='post_new'), #Url Config for blog form
    path('post/<int:pk>/edit/', BlogUpdateView.as_view(), name='post_edit'), #URL Config for Editing Blog
    path('post/<int:pk>/delete/', BlogDeleteView.as_view(), name='post_delete'), #URL Config for deleting Blog


]
