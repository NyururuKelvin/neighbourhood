from django.contrib.auth.models import User
from django import forms
from .models import Post,Neighbourhood,Comment,Business,Profile,Post
from django.contrib.auth.forms import UserCreationForm

class SignUpForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    email = forms.EmailField(max_length=254, required=True)

    class Meta:
        model = User
        fields = ('email' ,'username','password1', 'password2', )

class UpdateUser(forms.ModelForm):
    email=forms.EmailField()
    class Meta:
        model=User
        fields=['username', 'email']
        
class UpdateProfile(forms.ModelForm):
    class Meta:
        model=Profile
        fields = ('first_name','last_name','bio','neighbourhood','email')

class CompanyForm(forms.ModelForm):
    class Meta:
        model = Business
        exclude = ['user','neighborhood']

class PostPost(forms.ModelForm):
    CHOICES = (('1', 'Amber',), ('2', 'Normal',))
    type = forms.ChoiceField(widget=forms.Select, choices=CHOICES)
    class Meta:
        model = Post
        fields = ('title','content','type')
    class Meta:
        model=Post
        fields=['image','title','post','type']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('comment',)
        