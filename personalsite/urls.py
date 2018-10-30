
from django.urls import path

from . import views

app_name = 'personalsite'

urlpatterns = [
    path('', views.index, name='index'),

]