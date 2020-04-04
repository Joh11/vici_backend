from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# Create your views here.

from .models import Company

def index(request):
    if not request.user.is_authenticated:
        return HttpResponse("You're not logged in. ")
    return HttpResponse("This is the index. Welcome {}".format(request.user.username))

def login_view(request):
    return render(request, 'viciapp/sign_in_up.html')

def login_process(request):
    email = request.POST['emailLogIn']
    password = request.POST['pwLogIn']
    if request.POST['submit'] == 'Sign In':
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            # TODO redirect
    elif request.POST['submit'] == 'Sign Up':
        # Create account
        confirm = request.POST['pwConfirm']
        company_name = request.POST['companyName']

        # TODO check passwords match
        # TODO handle exceptions request POST access
        
        user = User.objects.create_user(email, email, password)
        login(request, user) # Login the newly created user
    else:
        pass # TODO error page ?
    
    print(request.POST['submit'])
    return HttpResponse("POST : {}".format(dict(request.POST)))
