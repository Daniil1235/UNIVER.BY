from datetime import datetime
from dateutil.relativedelta import relativedelta

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
                licensee = License.objects.get(key=key)
                if not licensee.used:
                    request.user.license_key = License.objects.get(key=key)
                    request.user.licensed = True
                    request.user.save()
                    today = datetime.today()
                    if licensee.time_limit.name[0:2] == '12':
                        duration_months = int(licensee.time_limit.name[0:2])
                    else:
                        duration_months = int(licensee.time_limit.name[0])
                    expire_date = today + relativedelta(months=duration_months)

                    licensee.expire_date = expire_date
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
    return render(request, "premium/activate.html", {"form": form, "range": range(1, 7)})
