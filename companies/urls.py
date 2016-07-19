from django.conf.urls import url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from companies import views

urlpatterns = [
    url(r'^stock/', views.StockList)
]

