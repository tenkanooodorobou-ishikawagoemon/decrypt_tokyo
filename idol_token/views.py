from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from .models import Idol, Idol_Item
import json

# Create your views here.
def top(request):
    data = list(Idol.objects.all()[:4].values('id', 'name', 'image', 'address', 'construct_id'))
    return JsonResponse({'data': data})

# Show the 'Idol' page
def idol(request, idol_id):
    data = list(Idol.objects.filter(id = idol_id).values('id', 'name', 'image', 'address', 'construct_id'))
    return JsonResponse({'data': data})

# Show all Idol data
def all_idol(request):
    data = list(Idol.objects.all().values('id', 'name', 'image', 'address', 'construct_id'))
    return JsonResponse({'data': data})

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

# Resist Idol
def register_idol(request):
    if request.method == 'POST':
        params = request.POST
        name = params.get('name')
        image = request.FILES.get('image')
        ret = cloudinary.uploader.upload(image, public_id='samplename', format='png', api_key='547257318196367', api_secret='ns0Zb5YWq5I2DMv8i6PNSE0DRHo', cloud_name='hlimgugdc')
        address = params.get('address')
        url = ret['secure_url']
        idol = Idol.objects.create(
            name = name,
            image = url,
            address = address,
            )
        data = {
            'id': idol.id,
        }
        return JsonResponse(data)

def register_item(request):
    if request.method == 'POST':
        params = request.POST
        title = params.get('title')
        image = request.FILES.get('image')
        ret = cloudinary.uploader.upload(image, public_id='samplename', format='png', api_key='547257318196367', api_secret='ns0Zb5YWq5I2DMv8i6PNSE0DRHo', cloud_name='hlimgugdc')
        url = ret['secure_url']

        item = Idol_Item.objects.create(
            title=title,
            image=url
        )

        data = {
            'id': item.id
        }

        return JsonResponse(data)

def purchace_item(request):
    if request.method == 'POST':
        params = request.POST
        token = params.get('tokenID')
        item = params.get('itemID')

        item = Idol_Item.objects.get(id=item)
        item.token = token
        token.save()

        data = {
            'id': item.id,
        }

        return JsonResponse(data)
