from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone

class Blog(models.Model):

    title = models.CharField(max_length=10)
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
