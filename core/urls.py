from django.urls import path,include
from .views import train,test

app_name="core"

urlpatterns = [
    path('train/',train,name='train'),
    path('test/',test,name='train')
]
