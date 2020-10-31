from django.db import models
from django.contrib.auth.models import User

# Models
class Neighbourhood(models.Model):
    admin=models.ForeignKey(User, on_delete=models.CASCADE)
    name=models.CharField(max_length=60)
    location = models.ForeignKey('Location',on_delete = models.CASCADE)
    occupants=models.IntegerField(default=0)

    def save_neighbourhood(self):
        self.save()

    def __str__(self):
        return self.name

    def create_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls,neigborhood_id):
        neighborhood = cls.objects.get(id = neigborhood_id)
        return neighborhood

    def update_neighborhood(self):
        self.save()

    def update_occupants(self):
        self.occupants += 1
        self.save()

class Business(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    name =models.CharField(max_length=60)
    description = models.CharField(max_length = 150,null=True)
    category = models.ForeignKey('Category',on_delete = models.CASCADE,null=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
    email =models.EmailField(max_length=60, blank=True)

    def __str__(self):
        return self.name

    def create_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def search_business(cls,search_term):
        business = Business.objects.get(name__icontains=search_term)
        return business

    def update_company(self):
        self.save()

class Post(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    image=models.ImageField(upload_to='post/', default='No image')
    title=models.CharField(max_length=60)
    post=models.TextField()
    type = models.CharField(max_length = 50,null=True)
    neighborhood = models.ForeignKey(Neighbourhood,on_delete = models.CASCADE)
    posted=models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.title

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
    first_name = models.CharField(max_length = 50,null=True)
    last_name = models.CharField(max_length = 50,null=True)
    bio = models.TextField(null=True)
    image=models.ImageField(upload_to='profile/', default='default.png')
    email=models.EmailField(max_length=60, blank=True)
    
    def __str__(self):
        return self.user.username
    
    def save_profile(self):
        self.save()

class Location(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length = 40)

    def __str__(self):
        return self.name


