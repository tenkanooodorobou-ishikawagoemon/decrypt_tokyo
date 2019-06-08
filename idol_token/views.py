from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from .models import Idol, Idol_Item
import json

# Create your views here.
def top(request):
    data = list(Idol.objects.all()[:4].values("id", "name", "image", "address", "construct_id"))
    return JsonResponse({"data": data})

# Show the "Idol" page
def idol(request, idol_id):
    data = list(Idol.objects.filter(id = idol_id).values("id", "name", "image", "address", "construct_id"))
    return JsonResponse({"data": data})

# Show all Idol data
def all_idol(request):
    data = list(Idol.objects.all().values("id", "name", "image", "address", "construct_id"))
    return JsonResponse({"data": data})

def get_idol(request, pk=None):
    idol = Idol.objects.get(address=pk).values('id', 'name', 'image', 'address')
    data = {
        'data': idol
    }

    return JsonResponse(data)

def get_index(request):
    recomends = Idol.objects.all()[4:].values('id', 'name', 'image', 'address')

    ranking = Idol.objects.all()[:4].values('id', 'name', 'image', 'address')

    data = {
        'recomends': recomends,
        'ranking': ranking
    }
    return JsonResponse(data)


def register_item(request):
    if request.method == 'POST':
        params = request.POST
        title = params.get('title')
        address = params.get('address')
