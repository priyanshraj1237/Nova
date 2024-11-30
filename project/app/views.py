from django.shortcuts import render,HttpResponse

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
        print(f"Name: {name}, Email: {email}, Phone: {phone}, Age: {age}, Experience: {experience}, Bio: {bio}")
        return HttpResponse("Registration successful!")
    return render(request,'app/register.html')

def signin(request):
    return render(request,'app/signin.html')

def choice(request):
    return render(request,'app/choice.html')

def learning(request):
    return render(request,'app/learning.html')

