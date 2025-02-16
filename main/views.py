from django.shortcuts import render, redirect, HttpResponse
from .forms import NewUserForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
import datetime
from calendar import monthrange
from .models import Type


def cur_date(request):
    date = datetime.date.today()
    year = date.year
    month = date.month
    day = date.day
    return {"year": year,
            "month": month,
            "day": day}


def check_license(request):
    user = request.user
    expire_soon = False
    days_left = 0
    expired = False
    if user.is_authenticated and user.licensed:
        day = user.license_key.expire_date.day
        month = user.license_key.expire_date.month
        year = user.license_key.expire_date.year
        today = datetime.datetime.today()

        expiry_date = datetime.datetime(year, month, day)
        days_left = (expiry_date - today).days + 1
        expire_soon = True if days_left <= 15 else False
        if days_left <= 0:
            expired = True
            expire_soon = False
            user.license_key.expired = True
            user.license_key.save()
            user.license_key = None
            user.licensed = False
            user.save()
    return {"expire_soon": expire_soon, "days_left": days_left, "expired": expired}


def index(request):
    return render(request, "main/index.html")



def about(request):
    return render(request, "main/about.html")


def register_request(request):
    red = request.GET.get('red')
    red = "home" if red is None else red
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Успешная регистрация")
            return redirect(red)
        messages.error(request, "При регистрации произошла ошибка. Убедитесь, что данные введены верно")
    form = NewUserForm()
    return render(request=request, template_name="main/register.html", context={"form": form, "types": Type.objects.all()})


def login_request(request):
    red = request.GET.get('red')
    red = "home" if red is None else red
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Вы успешно вошли как {username}")
                return redirect(red)
            else:
                messages.error(request, "Неверное имя или пароль")
        else:
            messages.error(request, "Неверное имя или пароль")
    return render(request=request, template_name="main/login.html")


def logout_request(request):
    red = request.GET.get('red')
    red = "home" if red is None else red
    logout(request)
    messages.warning(request, "Вы вышли из аккаунта")
    return redirect(red)
