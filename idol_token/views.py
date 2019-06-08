from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from .models import Idol, Idol_Item
import json

# Create your views here.
def top(request):
    data = list(Idol.objects.all()[:4].values("name", "image", "address", "construct_id"))
    return JsonResponse({"data": data})

# Show the "Idol" page
def idol(request, idol_id):
    data = list(Idol.objects.filter(id = idol_id).values("name", "image", "address", "construct_id"))
    return JsonResponse({"data": data})

# Show all Idol data
def all_idol(request):
    data = list(Idol.objects.all().values("name", "image", "address", "construct_id"))
    return JsonResponse({"data": data})

# For Idol page
def idol_page(request):
    if request.method != "POST":
        return redirect(to = "/idol_token")
