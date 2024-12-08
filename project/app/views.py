from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Register 
from django.http import HttpResponseRedirect

# Create your views here.
def landpage(request):
    return render(request,'app/landpage.html')


def register(request):
    if request.method == 'POST':
        # Get form data from the request
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        experience = request.POST.get('experience')
        bio = request.POST.get('bio')
        try:
            register_entry = Register(
                name=name,
                email=email,
                phone=phone,
                age=age,
                experience=experience,
                bio=bio
            )
            register_entry.save()
            messages.success(request, f"{name} Registration successful!")
            return render(request,'app/signin.html')
        except Exception as e:
            return HttpResponse(f"An error occurred: {e}")
    return render(request, 'app/register.html')
    

def signin(request):
    if request.method == 'POST':
        useremail = request.POST['useremail']
        password = request.POST['password']
        return redirect('choice')
    else:
            messages.error(request, "Invalid email address.")
    return render(request, 'app/signin.html')

def choice(request):
    if request.method == 'POST':
        user_type = request.POST.get('user_type')
        
        if user_type == 'learning':
            return HttpResponseRedirect("https://karan23831.github.io/zeepo-learn") #https://karan23831.github.io/zeepo-learn/
        elif user_type == 'buisness':
             return HttpResponseRedirect("https://skill-link-part2.vercel.app")
        else:
            return HttpResponse("Invalid user type", status=400) 
    return render(request,'app/choice.html')

def learning(request):
    return render(request,'app/learning.html')

def learning_video(request):
    return render(request,'app3/video.html')

def courses(request):
    return render(request, 'app3/courses.html')

def buisness(request):
    return render(request,'app/dashboard.html')

def earn(request):
    return HttpResponseRedirect("https://skill-link-part2.vercel.app/earn/jobsearch.html")

def learn(request):
    return HttpResponseRedirect("https://karan23831.github.io/zeepo-learn/")


