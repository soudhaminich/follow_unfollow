from django.db import models

# Create your models here.

from profiles.models import Profile
# Create your models here.

class Post(models.Model):
    
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.body)[:30]
   

    class Meta:
        ordering = ('-created',)

