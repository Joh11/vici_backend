from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render

# Create your views here.

from .models import Company

def index(request):
    return HttpResponse("This is the index. Welcome les garcons")

def create_company(request):
    return HttpResponse("Here you create your own page")

def register_company(request):
    pass # TODO

def details(request, company_id):
    company = get_object_or_404(Company, pk=company_id)
    return render(request, 'viciapp/details.html', {'company': company})

def all_companies(request):
    companies = Company.objects.all()
    output = ', '.join([c.name for c in companies])
    return HttpResponse(output)

def create_account(request):
    return render(request, 'viciapp/create_account.html')

def register_account(request):
    return HttpResponse('This is a response {}'.format(len(request.POST)))
