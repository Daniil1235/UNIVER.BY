from django.shortcuts import render


def premium_index(request):
    return render(request, "premium/premium.html")


def pricing(request):
    return render(request, "premium/pricing.html")


def premium_buy(request):
    return render(request, "premium/premium_buy.html")


def premium_activate(request):
    red = request.GET.get('red')
    red = "" if red is None else red
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
    return render(request, "premium/activate.html")