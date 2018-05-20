from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from xujia.models.roast.roast import Roast
import logging


def index(request):
    return render(request, 'article/index.html')


def publish(request):
    return render(request, 'article/publish.html')

