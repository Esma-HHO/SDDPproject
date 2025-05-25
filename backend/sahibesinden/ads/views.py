from django.shortcuts import get_object_or_404, render,redirect
from .models import Car, House, Furniture
from .forms import CarForm, HouseForm, FurnitureForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
User = get_user_model()

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


from .forms import CarForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

@login_required
def add_car(request):
    if request.method == 'POST':
        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.user = request.user  # Sadece 'user' alanını kullan
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

from django.contrib.contenttypes.models import ContentType
from django.shortcuts import get_object_or_404, redirect, render
from .models import Message
from django.contrib.auth.decorators import login_required

@login_required
def send_message(request, model_name, object_id):
    model = ContentType.objects.get(model=model_name).model_class()
    listing = get_object_or_404(model, id=object_id)
    receiver = listing.owner  # veya listing.created_by, modeline göre

    if request.method == 'POST':
        content = request.POST.get('content')
        message = Message.objects.create(
            sender=request.user,
            receiver=receiver,
            content_type=ContentType.objects.get_for_model(model),
            object_id=listing.id,
            content=content
        )

        # Mail gönderme fonksiyonu
        def send_message_email(sender, receiver, message):
            subject = 'Yeni Bir Mesajınız Var!'
            message_body = f"""
Merhaba {receiver.username},

{sender.username} size yeni bir mesaj gönderdi:

"{message.content}"

İlan: {listing}
Mesajı görmek için siteye giriş yapabilirsiniz.

İyi günler!
"""
            send_mail(
                subject,
                message_body,
                settings.EMAIL_HOST_USER,
                [receiver.email],
                fail_silently=True,
            )

        # Alıcıya mail gönder
        send_message_email(request.user, receiver, message)
        # İstersen satıcı da mesajdan haberdar olmalı diyorsan, örneğin burada kendi mailine gönderebilir:
        # send_message_email(receiver, request.user, message)

        return redirect('listing_detail', model_name=model_name, id=object_id)

    return render(request, 'ads/send_message.html', {'listing': listing, 'receiver': receiver})

@login_required
def inbox(request):
    messages = Message.objects.filter(receiver=request.user).order_by('-sent_at')
    filtered_messages = []
    for msg in messages:
        if msg.listing:
            msg.model_name = msg.listing._meta.model_name
            msg.listing_id = msg.listing.id
            filtered_messages.append(msg)
        else:
            msg.model_name = None
            msg.listing_id = None
            filtered_messages.append(msg)

    unread_count = Message.objects.filter(receiver=request.user, is_read=False).count()

    return render(request, 'ads/inbox.html', {
        'messages': filtered_messages,
        'unread_count': unread_count,
    })

from django.shortcuts import render, get_object_or_404
from django.apps import apps
@login_required
def listing_detail(request, model_name, id):
    return render(request, "ads/message_sent.html")

def reply_message(request, receiver_id):
    receiver = get_object_or_404(User, id=receiver_id)
    sender = request.user

    if request.method == 'POST':
        content = request.POST.get('content')
        if content:
            Message.objects.create(sender=sender, receiver=receiver, content=content)
            return redirect('inbox')
    return render(request, 'ads/reply_message.html', {'receiver': receiver})

from django.core.mail import send_mail
from django.conf import settings

def send_message_email(sender, receiver, message):
    subject = 'Yeni Bir Mesajınız Var!'
    message_body = f"""
    Merhaba {receiver.username},

    {sender.username} size yeni bir mesaj gönderdi:

    "{message.content}"

    Mesajı görmek için siteye giriş yapabilirsiniz.

    İyi günler!
    """
    send_mail(
        subject,
        message_body,
        settings.EMAIL_HOST_USER,
        [receiver.email],
        fail_silently=False,
    )