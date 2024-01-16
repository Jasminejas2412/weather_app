from django.urls import path
from . import views

urlpatterns = [
    path ('',views.weathert,name="weathert"),
    #path ('add',views.add,name="add"),
]