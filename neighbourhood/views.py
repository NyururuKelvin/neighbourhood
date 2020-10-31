from django.shortcuts import render,get_object_or_404,redirect
from django.http  import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Post,Business,User,Neighbourhood
from .forms import PostPost,UpdateUser,UpdateProfile,SignUpForm
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    posts = Post.objects.all()
    users = User.objects.all()
    return render(request, 'temps/index.html', {'posts': posts, 'users':users})

def about(request):
    return render(request, 'temps/about_us.html')

def profile(request):
    return render(request,'temps/profile.html')

def signup(request):
    name = "Sign Up"
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            name = form.cleaned_data.get('username')
            send_mail(
            'Welcome to Neighbourhood App.',
            f'Hello {name},\n '
            'Welcome to Neighbourhood App and have fun.',
            'nyururukelvin99@gmail.com@gmail.com',
            [email],
            fail_silently=False,
            )
        return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/registration_form.html', {'form': form, 'name':name})

def search_business(request):
    """
    Function that searches for projects
    """
    if 'business' in request.GET and request.GET["business"]:
        search_term = request.GET.get("business")
        searched_business = Project.objects.filter(title__icontains=search_term)
        message = f"{search_term}"
        businesses = Business.objects.all()
        
        return render(request, 'temps/search.html', {"message": message, "businesses": searched_business})

    else:
        message = "You haven't searched for any term"
        return render(request, 'temps/search.html', {"message": message})

def update_profile(request):

    profile = User(user=request.user)

    update_user=UpdateUser(request.POST,instance=request.user)
    update_profile=UpdateProfile(request.POST,request.FILES,instance=profile)
    if update_user.is_valid() and update_profile.is_valid():
        update_user.save()
        update_profile.save()
        
        messages.success(request, 'Profile Updated Successfully')
        return redirect('profile')
    
    else:
        update_user=UpdateUser(instance=request.user)
        update_profile=UpdateProfile(instance=profile)
    return render(request, 'temps/update_profile.html',{'update_user':update_user,'update_profile':update_profile})

def new_post(request):
    current_user=request.user
    if request.method=='POST':
        form=PostPost(request.POST,request.FILES)
        if form.is_valid():
            project=form.save(commit=False)
            project.user=current_user
            project.save()
        return redirect('index')
    
    else:
        form=PostPost()
        
    return render(request,'temps/new_post.html',{'form':form})