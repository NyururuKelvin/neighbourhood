from django.db import models
from django.contrib.auth.models import User

# Models
class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/', default='No image')
    title=models.CharField(max_length=60)
    post=models.TextField()
    posted=models.DateTimeField(auto_now_add=True) 

    def save_post(self):
        self.save()


class Comment(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE,)
    comment=models.CharField(max_length=255)
    posted=models.DateTimeField(auto_now_add=True) 

    @classmethod
    def get_comments(cls):
        comments = cls.objects.all()
        return comments

    def save_commment(self):
        self.save()

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile/', default='default.png')
    contact=models.CharField(max_length=30, blank=True)
    address=models.CharField(max_length=50,  blank=True)
    bio=models.TextField(blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()