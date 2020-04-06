from django.contrib.gis import forms
from .models import Company

# Choices
categories = ['Restaurant', 'Grocery', 'Fruits and Vegetables', 'Crafts', 'Florist', 'Clothes', 'Baker', 'Children', 'Food', 'Sport', 'Other']
categories = list(enumerate(categories))

service_categories = ['Direct Shopping', 'Online Shopping', 'Charity', 'Delivery', 'Map Pin', 'Other']
service_categories = list(enumerate(service_categories))

class CompanyForm(forms.Form):
    name = forms.CharField(max_length=200, label='Company name')
    description = forms.CharField(widget=forms.Textarea)
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 700, 'map_height': 500}))
    category = forms.ChoiceField(choices=categories) # TODO put list
    help_message = forms.CharField(widget=forms.Textarea, label='How can I get help') # blank=True
    opening_hours = forms.CharField() # max_length=400, blank=True

    # services
    service1_cat = forms.ChoiceField(choices=service_categories, label='Service # 1 category')
    service1_desc = forms.CharField(widget=forms.Textarea, label='Service # 1 description', required=False)

    service2_cat = forms.ChoiceField(choices=service_categories, label='Service # 2 category')
    service2_desc = forms.CharField(widget=forms.Textarea, label='Service # 2 description', required=False)

    service3_cat = forms.ChoiceField(choices=service_categories, label='Service # 3 category')
    service3_desc = forms.CharField(widget=forms.Textarea, label='Service # 3 description', required=False)

    
