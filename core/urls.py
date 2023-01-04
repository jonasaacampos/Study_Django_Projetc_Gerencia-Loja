from django.urls import path
from core.views import *

urlpatterns = [
    path("", index, name="home"),
    path("contato", contato, name="contato"),
    path("produto", produto, name="produto"),
]