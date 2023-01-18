import datetime

from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Game, Meeting
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
# Create your views here.

def index(request):
    return HttpResponse("index")


@login_required
def add_game(request):
    result = Game(name="Pierwsza gra",
    person_count=2,
    is_online=False,
    add_date=datetime.datetime.now()
    )
    result.save()
    return HttpResponse("ok")

@login_required()
def get_game(request):
    result = Game.objects.all()
    return HttpResponse(result)

@login_required()
def delete_game(request):
    try:
        result = Game.objects.get(name="Pierwsza gra").delete()
    except Game.DoesNotExist:
        return HttpResponse("Not Found")
    else:
        result = get_object_or_404(Game, name="Pierwsza gra").delete()
        return HttpResponse("deleted")

@csrf_exempt
def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    #return HttpResponse(f"{username}, {password}")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        #response = serialize("json", user, fields=(username, password))
        login(request, user)
        return HttpResponse("authorized")
    else:
        return HttpResponse("Bad credentials")

def permission_denied(request):
    return HttpResponse("Not authorized")
