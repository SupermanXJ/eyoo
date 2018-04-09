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
    user_id = request.session['user_id']
    logging.debug(user_id)
    logging.info(user_id)
    roasts = Roast.get_list(user_id)
    return JsonResponse({'roasts': roasts})
