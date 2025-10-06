from django.shortcuts import render
from datetime import datetime
from .models import FruitType

def home(request):
    return render(request, 'index.html')

def all_fruit(request):
    fruit = FruitType.object.all()
    return render(request, 'index.html',{'fruit':fruit})

def test(request):
    return render(request, 'test.html')



