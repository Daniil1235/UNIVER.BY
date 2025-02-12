import datetime
from django.shortcuts import render, redirect
from .forms import LicenseForm
from .models import License
from main.models import User
from django.contrib import messages


def premium_index(request):
    return render(request, "premium/premium.html")


def pricing(request):
    return render(request, "premium/pricing.html")


def premium_buy(request):
    return render(request, "premium/premium_buy.html")


# noinspection LongLine
def premium_activate(request):
    if request.method == "POST":
        form = LicenseForm(request, data=request.POST)
        if form.is_valid():
            key = form.cleaned_data.get("key")

            if License.objects.filter(key=key):
                request.user.license_key = License.objects.get(key=key)
                request.user.licensed = True
                request.user.save()
                licensee = License.objects.get(key=key)
                if not licensee.used:
                    date = datetime.date.today()
                    year = date.year
                    month = date.month
                    day = date.day

                    if licensee.time_limit.name == "12 месяцев":
                        licensee.expire_date = f"{year + 1}-{month}-{day}"
                    if licensee.time_limit.name == "6 месяцев":
                        if month <= 6:
                            licensee.expire_date = f"{year}-{month + 6}-{day}"
                        else:
                            ost = 12 - month
                            licensee.expire_date = f"{year + 1}-{1 + ost}-{day}"
                    if licensee.time_limit.name == "3 месяца":
                        if month <= 9:
                            licensee.expire_date = f"{year}-{month + 3}-{day}"
                        else:
                            ost = 12 - month
                            licensee.expire_date = f"{year + 1}-{1 + ost}-{day}"
                    if licensee.time_limit.name == "1 месяц":
                        if month <= 11:
                            licensee.expire_date = f"{year}-{month + 1}-{day}"
                        else:
                            ost = 12 - month
                            licensee.expire_date = f"{year + 1}-{1 + ost}-{day}"

                    licensee.used = True
                    licensee.save()
                    messages.success(request, "Ваша лицензия успешно активирована")
                    return redirect("premium_activate")
                else:
                    messages.error(request, "Этот ключ уже использован")
            else:
                messages.error(request, "Ключ указан неверно")
        else:
            messages.warning(request, "При обработке произошла ошибка")

    form = LicenseForm()
    return render(request, "premium/activate.html", {"form": form})
