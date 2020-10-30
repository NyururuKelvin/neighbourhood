from django.contrib import admin
from .models import Post,Profile,Comment

# Registering Models
admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(Comment)