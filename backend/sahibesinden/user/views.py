from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from .forms import SignUpForm, LoginForm
from django.contrib.sites.shortcuts import get_current_site  
from django.utils.http import urlsafe_base64_encode  
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes  
from django.contrib.auth.tokens import default_token_generator  
from django.core.mail import send_mail  
from django.contrib import messages  
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login


from .models import Member  

def verify_email(request, uidb64, token):
    User = get_user_model()
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.is_email_verified = True 
        user.save()
        return render(request, 'user/email_confirmed.html')  # başarı sayfası
    else:
        return render(request, 'user/email_invalid.html')  # geçersiz link sayfası


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)  
            user.is_active = False # kullanıcı aktif olmasın, mail onayı beklesin
            user.save()

            # 💖 Email gönderme işlemi
            current_site = get_current_site(request)
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            link = f"http://127.0.0.1:8000/users/verify-email/{uid}/{token}/"

            message = f"Merhaba {user.username},\n\nEmail adresini doğrulamak için linke tıkla:\n{link}"
            send_mail(
                'Email Doğrulama',
                message,
                'esmah.2004@gmail.com', 
                [user.email],
                fail_silently=False,
            )
            return render(request, 'user/confirmation_sent.html')  

    else:
        form = SignUpForm()
    return render(request, 'user/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            if not user.is_email_verified:  
                messages.error(request, 'Email adresin henüz doğrulanmadı.')  
                return redirect('login')  
            login(request, user)
            return redirect('home')
    else:
        form = LoginForm()
    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
