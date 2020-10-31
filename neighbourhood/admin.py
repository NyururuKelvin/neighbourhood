from django.contrib import admin
from .models import Post,Comment,Neighbourhood,Business,Profile

# Registering Models
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Neighbourhood)
admin.site.register(Business)
admin.site.register(Profile)