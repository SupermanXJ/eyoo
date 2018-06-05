from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponseRedirect
from django.db import connection
import logging
from xujia.models.users import Users


@csrf_protect
def register(request):
    Users.register(request.POST['email'], request.POST['password'])
    return render(request, 'index.html')


@csrf_protect
def login(request):
    email = request.POST['email']
    password = request.POST['password']
    login_user = Users.get_login_user(email, password)

    request.session['user_id'] = login_user[0]
    request.session['user_name'] = login_user[1]

    return HttpResponseRedirect('/')


def logout(request):
    del request.session['user_id']
    del request.session['user_name']
    return HttpResponseRedirect('/')
