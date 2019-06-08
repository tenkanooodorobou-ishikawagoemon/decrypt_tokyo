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

def get_idol(request):
    if request.method == 'GET':
        address = request.GET.get('address')
        idol = Idol.objects.filter(address=address).first()
        io = {
            'id': idol.id,
            'name': idol.name,
            'image': idol.image,
            'address': idol.address
        }

        return JsonResponse(io)

def get_index(request):
    recomends = Idol.objects.all().order_by('name')[4:].values('id', 'name', 'image', 'address')
    recomends_list = list(recomends)

    ranking = Idol.objects.all().order_by('-name')[4:].values('id', 'name', 'image', 'address')
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
        image = request.FILES.get('image')
        ret = cloudinary.uploader.upload(image, public_id='samplename', format='png', api_key='547257318196367', api_secret='ns0Zb5YWq5I2DMv8i6PNSE0DRHo', cloud_name='hlimgugdc')
        url = ret['secure_url']
        address = params.get('address')

        item = Idol_Item.objects.create(
            title=title,
            image=url
        )

        data = {
            'id': item.id
        }

        return JsonResponse(data)
