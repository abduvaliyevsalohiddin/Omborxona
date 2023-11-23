from django.shortcuts import render, redirect
from django.views import View
from .models import *
from accounts.models import *
from asosiy.models import *
from datetime import date


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

    def post(self, request):
        Statistika.objects.create(
            mahsulot=Mahsulot.objects.get(id=request.POST.get("mahsulot")),
            mijoz=Mijoz.objects.get(id=request.POST.get("mijoz")),
            miqdor=request.POST.get("miqdor"),
            summa=request.POST.get("summa"),
            tolangan_summa=request.POST.get("tolangan_summa"),
            sana=date.today(),
            nasiya=request.POST.get("nasiya"),
            ombor=request.user
        )
        return redirect("/stats/statislar/")


class StatsUpdateView(View):
    def get(self, request, son):
        if request.user.is_authenticated:
            stats = Statistika.objects.get(id=son)
            if stats.ombor == request.user:
                content = {
                    "mahsulotlar": Mahsulot.objects.filter(ombor=request.user),
                    "mijozlar": Mijoz.objects.filter(ombor=request.user),
                    "stats": Statistika.objects.get(id=son)
                }
                return render(request, "stats_update.html", content)
            return redirect("/stats/statislar/")
        return redirect("/")

    def post(self, request, son):
        Statistika.objects.filter(id=son).update(
            miqdor=request.POST.get("miqdor"),
            summa=request.POST.get("summa"),
            tolangan_summa=request.POST.get("tolangan_summa"),
            nasiya=request.POST.get("nasiya"),
            sana=date.today(),
            ombor=request.user
        )
        return redirect("/stats/statislar/")
