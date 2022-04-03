from email import message
from django.shortcuts import render
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home(request):
    if request.method == "POST":
        if "register-form" in request.POST:
            username = request.POST.get("username")
            email = request.POST.get("email")
            password = request.POST.get("password")
            password2 = request.POST.get("password2")

            if password != password2: 
                msg = "Passwords do not match!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)

            elif User.objects.filter(username=username).exists():
                msg = f"Username:{username} already exists!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)

            elif User.objects.filter(email=email).exists():
                msg = f"Email:{email} already exists!"
                messages.error(request, msg)
                return HttpResponseRedirect(request.path)

            else:
                User.objects.create_user(username, email, password)
                new_user = authenticate(request, username=username, password=password2)
                if new_user is not None:
                    login(request, new_user)
                    msg = f"Hey, {username}! Welcome to Secretary!"
                    messages.success(request, msg)
                    return HttpResponseRedirect(request.path)

    return render(request, "home.html", {})
