
from django.contrib import admin
from django.urls import path,include
from .views import Modelview
app_name="modelstore"

urlpatterns = [
    path('',Modelview.as_view()),
]
