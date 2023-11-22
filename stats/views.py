from django.shortcuts import render, redirect
from django.views import View
from .models import *
from accounts.models import *
from asosiy.models import *


class StatisView(View):
    def get(self, request):
        if request.user.is_authenticated:
            content = {
                "statistikalar": Statistika.objects.filter(ombor=request.user),
                "mahsulotlar": Mahsulot.objects.filter(ombor=request.user),
                "mijozlar": Mijoz.objects.filter(ombor=request.user),
                "nom": request.user.nom.capitalize()
            }
            return render(request, "stats.html", content)
        return redirect("/")
