from django.http import HttpResponse
from django.shortcuts import render
from fitness.models import Equipment

def equipment_list(request):
    return HttpResponse('ok')
