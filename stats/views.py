from django.shortcuts import render
from django.views import View


class StatisView(View):
    def get(self, request):
        return render(request, "stats.html")
