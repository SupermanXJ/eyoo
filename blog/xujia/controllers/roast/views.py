from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from xujia.models.roast.roast import Roast
import logging


def index(request):
    return render(request, 'roast/index.html')


@csrf_exempt
def api_talk(request):
    Roast.insert(1, request.POST['content'])
    return JsonResponse({'result': True})


@csrf_exempt
def api_get_list(request):
    roasts = Roast.get_list()
    return JsonResponse({'roasts': roasts})
