from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.views.generic import UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages


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
    return render(request=request, template_name="main/register.html", context={"register_form": form})


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
    form = AuthenticationForm()
    return render(request=request, template_name="main/login.html", context={"login_form": form})


def logout_request(request):
    red = request.GET.get('red')
    red = "home" if red is None else red
    logout(request)
    messages.warning(request, "Вы вышли из аккаунта")
    return redirect(red)