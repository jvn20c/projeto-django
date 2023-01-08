from django.urls import path
from recibos.views import inicio, contato, sobre

urlpatterns = [
    path('', inicio),
    path('contato/', contato),
    path('sobre/', sobre),
]