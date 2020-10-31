from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'temps/index.html')

def about(request):
    return render(request, 'temps/about_us.html')