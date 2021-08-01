from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    # path('', views.index, name="query-page1"),
    path('', views.home, name="query-page2"),
]
