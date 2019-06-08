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

def get_idol(request, pk=None):
    idol = Idol.objects.get(address=pk).values('id', 'name', 'image', 'address')
    data = {
        'data': idol
    }

    return JsonResponse(data)

def get_index(request):
    recomends = Idol.objects.all()[4:].order_by('name').values('id', 'name', 'image', 'address')
    recomends_list = list(recomends)

    ranking = Idol.objects.all()[4:].order_by('-name').values('id', 'name', 'image', 'address')
    ranking_data = list(ranking)

    data = {
        'recomends': recomends_list,
        'ranking': ranking_data
    }
    return JsonResponse(data)


def register_item(request):
    if request.method == 'POST':
        params = request.POST
        title = params.get('title')
        address = params.get('address')
