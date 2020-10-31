from django.db import models
from django.contrib.auth.models import User

# Models
class Neighbourhood(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    n_name=models.CharField(max_length=60)
    n_location=models.CharField(max_length=60)
    occupants_count=models.IntegerField(default=0)

    def save_neighbourhood(self):
        self.save()

class Business(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    b_name =models.CharField(max_length=60)
    b_neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    b_email =models.CharField(max_length=30, blank=True)

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
    neighbourhood=models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='profile/', default='default.png')
    name=models.CharField(max_length=150, blank=True)
    contact=models.CharField(max_length=30, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

