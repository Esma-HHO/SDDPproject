from django.shortcuts import get_object_or_404, render,redirect
from .models import Car, House, Furniture
from .forms import CarForm, HouseForm, FurnitureForm
from django.contrib.auth.decorators import login_required

def home(request):
    cars = Car.objects.all()
    houses = House.objects.all()
    furniture = Furniture.objects.all()
    return render(request, 'ads/home.html', {
        'cars': cars,
        'houses': houses,
        'furniture': furniture,
    })

def car_list(request):
    cars = Car.objects.all()
    return render(request, 'ads/car_list.html', {'cars': cars})

def house_list(request):
    houses = House.objects.all()
    return render(request, 'ads/house_list.html', {'houses': houses})

def furniture_list(request):
    furniture = Furniture.objects.all()
    return render(request, 'ads/furniture_list.html', {'furniture': furniture})


@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = request.user
            car.user = request.user
            car.save()
            return redirect('home')
        else:
            print(form.errors)
    else:
        form = CarForm()
    return render(request, 'ads/ad_car.html', {'form': form})

@login_required
def like_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    user = request.user 
    if user in car.liked_by.all():
        car.liked_by.remove(user)  # Beğendiyse geri çek
    else:
        car.liked_by.add(user)     # Beğen
    return redirect('car_list')

def delete_car(request, car_id):
    car = get_object_or_404(Car, id=car_id)
    if car.user == request.user:
        car.delete()
        return redirect('car_list') 
    else:
        return redirect('car_list')

@login_required
def add_house(request):
    if request.method == 'POST':
        form = HouseForm(request.POST)
        if form.is_valid():
            house = form.save(commit=False)
            house.owner = request.user
            house.user = request.user
            house.save()
            return redirect('home')
    else:
        form = HouseForm()
    return render(request, 'ads/ad_house.html', {'form': form})

@login_required
def like_house(request, house_id):
    house = get_object_or_404(House, id=house_id)
    user = request.user
    if user in house.liked_by.all():
        house.liked_by.remove(user)
    else:
        house.liked_by.add(user)
    return redirect('house_list')

def delete_house(request, house_id):
    house = get_object_or_404(House, id=house_id)
    if house.user == request.user:
        house.delete()
        return redirect('house_list')  
    else:
        return redirect('house_list')
    
@login_required
def add_furniture(request):
    if request.method == 'POST':
        form = FurnitureForm(request.POST)
        if form.is_valid():
            furniture = form.save(commit=False)
            furniture.owner = request.user
            furniture.user = request.user
            furniture.save()
            return redirect('home')
    else:
        form = FurnitureForm()
    return render(request, 'ads/ad_furniture.html', {'form': form})

@login_required
def like_furniture(request, furniture_id):
    furniture = get_object_or_404(Furniture, id=furniture_id)
    user = request.user
    if user in furniture.liked_by.all():
        furniture.liked_by.remove(user)
    else:
        furniture.liked_by.add(user)
    return redirect('furniture_list')

def delete_furniture(request, furniture_id):
    furniture = get_object_or_404(Furniture, id=furniture_id)
    if furniture.user == request.user:
        furniture.delete()
        return redirect('furniture_list')  
    else:
        return redirect('furniture_list')