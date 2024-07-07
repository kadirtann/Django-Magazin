from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User
from .models import Writer, Reader

def login(request):
    if request.method == 'POST':
        login_info = request.POST.get('username')
        password = request.POST.get('password')
        
        if not login_info or not password:
            messages.error(request, 'Kullanıcı adı ve şifre gereklidir.')
            return render(request, 'login/login.html')
        
        try:
            user_mail = User.objects.get(email=login_info)
            user = authenticate(request, username=user_mail.username, password=password)
        except User.DoesNotExist:
            user = authenticate(request, username=login_info, password=password)
        
        if user is not None:
            try:
                writer = Writer.objects.get(user=user)
                auth_login(request, user)
                return redirect('index')
            except Writer.DoesNotExist:
                try: 
                    reader = Reader.objects.get(user=user)
                    auth_login(request, user)
                    return redirect('index')
                except Reader.DoesNotExist:
                    messages.error(request, 'Kullanıcı mevcut ancak Okur veya Yazar değil.')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış!')
    return render(request, 'login/login.html')


def register_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        password = request.POST.get('password1')
        confirm_password = request.POST.get('password2')
    
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Kullanıcı adı zaten mevcut!')
            elif User.objects.filter(email=email).exists():
                messages.error(request, 'Email zaten mevcut!')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, email=email, password=password)
                user.save()
                reader = Reader.objects.create(user=user, phone=phone)
                reader.save()
                auth_login(request, user)
                return redirect('index')
        else:
            messages.error(request, 'Şifreler eşleşmiyor!')
    
    return render(request, 'login/login.html')

def base(request):
    return render(request, 'main/base.html')

def index(request):
    return render(request, 'main/index.html')