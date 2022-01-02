from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name ='home'),
    path('about', views.about, name ='about'),
    path('locations', views.locations, name ='locations'),
    path('maintenance', views.maintenance, name ='maintenance'),
    path('price', views.price, name ='price'),
    path('repair', views.repair, name ='repair'),
    path('repair_info', views.repair_info, name ='repair_info'),

]