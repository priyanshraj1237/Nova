from django.shortcuts import render,HttpResponse

# Create your views here.
def landpage(request):
    return render(request,'app/landpage.html')


def register(request):
    return render(request,'app/register.html')

def signin(request):
    return render(request,'app/signin.html')

def choice(request):
    return render(request,'app/choice.html')

def learning(request):
    return render(request,'app/learning.html')

