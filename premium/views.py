from django.shortcuts import render


def premium_index(request):
    return render(request, "premium/premium.html")


def pricing(request):
    return render(request, "premium/pricing.html")


def premium_buy(request):
    return render(request, "premium/premium_buy.html")


def premium_activate(request):
    return render(request, "premium/activate.html")