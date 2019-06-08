from django.shortcuts import render
from django.shortcuts import redirect
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from .models import Idol, Idol_Item
import json

# Create your views here.
def top(request):
    return HttpResponse("Hello, World!!!")

def test(request):
    test = Idol.objects.all().values('name', 'image', 'construct_id')
    data = list(test)
    return JsonResponse({"data": data})
