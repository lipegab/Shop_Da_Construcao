from django.shortcuts import render
from django.utils import timezone

from .models import BlogTip, Offer, Partner


def home(request):
    today = timezone.localdate()
    context = {
        "offers": Offer.objects.filter(
            active=True,
            valid_from__lte=today,
            valid_until__gte=today,
        )[:3],
        "tips": BlogTip.objects.filter(published=True)[:3],
        "partners": Partner.objects.filter(active=True)[:4],
    }
    return render(request, "catalog/home.html", context)


def offers(request):
    today = timezone.localdate()
    return render(
        request,
        "catalog/offers.html",
        {
            "offers": Offer.objects.filter(
                active=True,
                valid_from__lte=today,
                valid_until__gte=today,
            )
        },
    )


def careers(request):
    return render(request, "catalog/careers.html")


def tips(request):
    return render(
        request,
        "catalog/tips.html",
        {"tips": BlogTip.objects.filter(published=True)},
    )


def partners(request):
    return render(
        request,
        "catalog/partners.html",
        {"partners": Partner.objects.filter(active=True)},
    )
