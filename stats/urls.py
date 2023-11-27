from django.urls import path
from .views import *

urlpatterns = [
    path("statislar/", StatisView.as_view()),
    path("stats_update/<int:son>/", StatsUpdateView.as_view()),
    path("stats_delete/<int:son>/", DeleteStatis.as_view()),

]
