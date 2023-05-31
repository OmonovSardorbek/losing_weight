from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as login_user, logout as log_out
from .models import APPUser
from django.contrib import messages


# Create your views here.
def create_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if not APPUser.objects.filter(username=username).exists():
                APPUser.objects.create_user(username=username, password=password1)
                user = authenticate(request, username=username, password=password1)
                if user is not None:
                    login_user(request, user)
                    return redirect('dashboard')
            else:
                messages.error(request, "Bunday foydalanuvhi mavjud!")
                return redirect('create-user')
            return redirect('dashboard')
        else:
            messages.error(request, "Parol bir xil emas!")
            return redirect('create-user')
    return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login_user(request, user)
            return redirect('dashboard')

    return render(request, 'accounts/login.html')


def logout(request):
    log_out(request)
    return redirect('dashboard')
