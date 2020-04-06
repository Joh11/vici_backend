from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404, render, redirect

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from tastypie.models import ApiKey

# Create your views here.

from .models import Company, Image, Service
from .forms import CompanyForm



def index(request):
    return render(request, 'viciapp/index.html')

def about(request):
    return render(request, 'viciapp/about.html')

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
    return redirect('viciapp:edit_profile')

# def edit_profile(request):
#     return render(request, 'viciapp/edit_profile.html')

def tac(request):
    return render(request, 'viciapp/terms_and_conditions')

def edit_profile(request):
    if not request.user.is_authenticated:
        return redirect('viciapp:login')
    
    if request.method == 'POST':
        form = CompanyForm(request.POST, request.FILES)

        if form.is_valid():
            # Add the company
            c = form.cleaned_data
            company = Company(user=request.user, name=c['name'], description=c['description'], location=c['location'], category=c['category'], help_message=c['help_message'], opening_hours=c['opening_hours'])
            
            if c['service1_desc']:
                service1 = Service(company=company, category=c['service1_cat'], description=c['service1_desc'])
            if c['service2_desc']:
                service2 = Service(company=company, category=c['service2_cat'], description=c['service2_desc'])
            if c['service3_desc']:
                service3 = Service(company=company, category=c['service3_cat'], description=c['service3_desc'])
                            
            # remove previous company and services
            Service.objects.filter(company__user=request.user).delete()
            Company.objects.filter(user=request.user).delete()

            # remove all previous images
            Image.objects.filter(company__user=request.user).delete()

            logo = Image(company=company, legend='logo', image=c['logo'])
            cover = Image(company=company, legend='cover', image=c['cover'])
            
            company.save()
            logo.save()
            cover.save()

            for i in [1, 2, 3]:
                key = 'other_image{}'.format(i)
                if c[key]:
                    image = Image(company=company, legend='other_images', image=c[key])
                    image.save()
            
            if c['service1_desc']:
                service1.save()
            if c['service2_desc']:
                service2.save()
            if c['service3_desc']:                
                service3.save()
            return redirect('viciapp:index')
    else:
        initial = {}
        if hasattr(request.user, 'company'):
            c = request.user.company
            initial['name'] = c.name
            initial['description'] = c.description
            initial['location'] = c.location
            initial['category'] = c.category
            initial['help_message'] = c.help_message
            initial['opening_hours'] = c.opening_hours
            
        form = CompanyForm(initial=initial)

    return render(request, 'viciapp/edit_profile.html', {'form': form})

def logout(request): # LOGOUT TODO
    if request.user.is_authenticated:
        logout(request.user)
    return redirect(index)

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
    
