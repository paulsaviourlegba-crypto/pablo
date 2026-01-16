from django.shortcuts import render,redirect
from .models import JobApplication
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
    return render (request, "index.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('signin')
    return render (request, "signin.html")

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            return redirect ('index')
        if User.objects.filter(username=username).exists():
            return redirect('index')
        if User.objects.filter(email=email).exists():
            return redirect ('index')
        
        user = User.objects.create_user(username=username, email=email, password=password1)

        user.save
        login(request, user)
        return redirect('index')

    return render (request, "signup.html")

def career(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        email = request.POST.get('email')
        cover_letter = request.POST.get('cover_letter')
        resume = request.FILES.get('resume')
        profile_picture = request.FILES.get ('profile_pic')

        JobApplication.objects.create(
            full_name = full_name, email = email, cover_letter = cover_letter, resume = resume, 
            profile_picture = profile_picturex
        )
        return redirect('index')
    return render (request, "career.html")