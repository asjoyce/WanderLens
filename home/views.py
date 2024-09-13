from django.shortcuts import render

def homepage(request):
    return render(request, '/Users/sathwikajoyce/WanderLens/home/templates/home.html')

def slideshow(request):
    return render(request, 'slideshow.html')
# Create your views here.
