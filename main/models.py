from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

# Create your models here.

class Article(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=150)
    body = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        permissions = [
            ('can_view_author', "Can View Article Author"),
        ]
    def __str__(self):
        return  self.title
    
    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"article_id": self.id})
    

    
    