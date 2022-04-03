import random
import math
from email import message
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail

def OTP_code_generator():
    digits="0123456789"
    OTP=""
    for i in range(6):
        OTP+=digits[math.floor(random.random()*10)]
    return OTP

# Create your views here.
def home(request):
    if request.method == "POST":
        if "register-form" in request.POST:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")
            if password != password2: 
                msg = "Registration Failed: Passwords do not match"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            elif User.objects.filter(username=username).exists():
                msg = f"Registration Failed: {username} already exists"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            elif User.objects.filter(email=email).exists():
                msg = f"Registration Failed: {email} already exists"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            else:
                User.objects.create_user(username, email, password)
                new_user = authenticate(request, username=username, password=password2)
                if new_user is not None:
                    login(request, new_user)
                    msg = f"Login succeeded: {username}, welcome to Secretary"
                    messages.success(request, msg)
                    return HttpResponseRedirect(request.path)

        elif "logout" in request.POST:
            msg = f"Logout succeeded: {request.user}, see you again"
            logout(request)
            messages.success(request, msg)
            return HttpResponseRedirect(request.path)

        elif 'login-form' in request.POST:
            username = request.POST.get("username")
            password = request.POST.get("password")
            new_login = authenticate(request, username=username, password=password)
            if new_login is None:
                msg = f"Login Failed: Your username or password is incorrect"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)
            else:
                otp = OTP_code_generator()
                global global_OTP
                global_OTP = otp
                send_mail(
                    "Secretary Password Manager: Email Confirmation",
                    f"{otp} is your OTP",
                    settings.EMAIL_HOST_USER,
                    [new_login.email],
                    fail_silently=False,
                )
                return render(request, "home.html", {
                    "code":otp, 
                    "user" :new_login,
                })

    return render(request, "home.html", {})
