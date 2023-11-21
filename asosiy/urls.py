from django.urls import path
from .views import *

urlpatterns = [
    path("bolimlar/", BolimlarView.as_view()),
    path("mahsulotlar/", MahsulotlarView.as_view()),
    path("clientlar/", MijozlarView.as_view()),
    path("mahsulotlar_update/<int:son>/", MahsulotlarUpdateView.as_view())

]
