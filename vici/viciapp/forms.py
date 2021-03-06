from django.contrib.gis import forms
from .models import Company

# Choices
categories = ['Restaurant', 'Grocery', 'Fruits and Vegetables', 'Crafts', 'Florist', 'Clothes', 'Baker', 'Children', 'Food', 'Sport', 'Other']
categories = list(enumerate(categories))

service_categories = ['Direct Shopping', 'Online Shopping', 'Charity', 'Delivery', 'Map Pin', 'Other']
service_categories = list(enumerate(service_categories))

class CompanyForm(forms.Form):
    name = forms.CharField(max_length=200, label='Company name')
    logo = forms.ImageField(label='Logo')
    description = forms.CharField(widget=forms.Textarea)
    location = forms.PointField(widget=forms.OSMWidget(attrs={'map_width': 700, 'map_height': 500}))
    category = forms.ChoiceField(choices=categories) # TODO put list
    help_message = forms.CharField(widget=forms.Textarea, label='How can I get help') # blank=True
    opening_hours = forms.CharField() # max_length=400, blank=True

    cover = forms.ImageField(label='Cover picture')

    other_image1 = forms.ImageField(label='Other image # 1', required=False)
    other_image2 = forms.ImageField(label='Other image # 2', required=False)
    other_image3 = forms.ImageField(label='Other image # 3', required=False)
    
    # services
    service1_cat = forms.ChoiceField(choices=service_categories, label='Service # 1 category')
    service1_desc = forms.CharField(widget=forms.Textarea, label='Service # 1 description', required=False)

    service2_cat = forms.ChoiceField(choices=service_categories, label='Service # 2 category')
    service2_desc = forms.CharField(widget=forms.Textarea, label='Service # 2 description', required=False)

    service3_cat = forms.ChoiceField(choices=service_categories, label='Service # 3 category')
    service3_desc = forms.CharField(widget=forms.Textarea, label='Service # 3 description', required=False)
