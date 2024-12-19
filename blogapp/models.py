from django.db import models
from django.urls import reverse

# Creating model Post with the required fields
class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()

    def __str__(self):
        return self.title
    
    #Resolve the URL dynamically 
    def get_absolute_url(self):
        return reverse("post_detail", args=[str(self.id)])
    
    



