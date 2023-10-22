from django.urls import path
from . import views

urlpatterns = [
    path('equipments/', views.equipment_list)
]
