from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from tastypie.models import ApiKey

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

def edit_profile(request):
    return render(request, 'viciapp/edit_profile.html')

def logout(request): # LOGOUT TODO
    if request.user.is_authenticated:
        logout(request.user)
    return redirect(index)

def file_upload(request):
    return render(request, 'viciapp/file_upload.html')

def file_upload_process(request):
    for x in request.FILES:
        print(type(x))
        print(x)
        f = request.FILES[x]
        print(type(f))
        with open(x, 'wb+') as dest:
            for chunk in f.chunks():
                dest.write(chunk)
    return HttpResponse("request.FILES = {}".format(dict(request.FILES)))

# Tweak to make the api key retrievable from the app
@csrf_exempt # TODO REMOVE LATER
def login_app(request):
    """View responsible for giving the API key to the application, given a
    username and password. The format of the json response can be
    found in json/login_app_response.json. 
    """
    print('POST content : ')
    for x in request.POST:
        print("post key {}".format(x))
    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)

    success = False
    error_message = ""
    api_key = ""
    if user is not None:
        try:
            api_key = user.api_key
        except ApiKey.DoesNotExist:
            # if it did not work because there was no API key
            error_message = "User has no API key attached"
        # if it worked
        success = True
    else:
        # if wrong credentials
        error_message = "Wrong credentials"

    feedback = {'success': success, 'errorMessage': error_message, 'apiKey': api_key.key}
    response = JsonResponse(feedback)
    print(response.content)
    return response

# TODO untested ! 
@csrf_exempt # TODO REMOVE LATER
def sign_up_app(request):
    """The view responsible for creating an account from the
    application. It is different from the website login page, as it
    returns a json response with the API key.

    Will check if the credentials are valid, and will return the API
    key. A format of the response can be found in
    json/login_app_response.json
    """
    username = request.POST['username']
    email = request.POST['email']
    password = request.POST['password']

    # Predefine the response
    success = False
    error_message = ""
    api_key = ""

    user = User.objects.create_user(username, email, password)
    api_key = user.api_key.key

    feedback = {'success': success, 'errorMessage': error_message, 'apiKey': api_key.key}
    response = JsonResponse(feedback)
    print(response.content)
    return response
    
