from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("This is the index. Welcome")

def create_company(request):
    return HttpResponse("Here you create your own page")
