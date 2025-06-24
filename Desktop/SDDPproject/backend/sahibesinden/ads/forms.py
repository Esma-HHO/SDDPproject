from django import forms
from .models import Car, House, Furniture

class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = [
            'name', 'price', 'comments', 'bargaining', 'location',
            'brand', 'model', 'productionYear', 'millage',
            'transmission', 'fuelType', 'liked_by'
        ]

class HouseForm(forms.ModelForm):
    class Meta:
        model = House
        fields= ['name', 'price', 'comments', 'bargaining', 'location', 'rooms', 'size_m2', 'floor', 'buildYear', 'liked_by']

class FurnitureForm(forms.ModelForm):
    class Meta:
        model = Furniture
        fields = ['name', 'price', 'comments', 'bargaining', 'location', 'type', 'material','colour','liked_by']
