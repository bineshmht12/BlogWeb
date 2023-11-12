from django.shortcuts import redirect, reverse
from django.db import models
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=255)
    author =models.ForeignKey('auth.User', on_delete=models.CASCADE)
    
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("blog:post_detail", kwargs={"pk": self.pk})
    
    