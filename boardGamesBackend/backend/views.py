import datetime

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Game, Meeting
# Create your views here.
def index(request):
    return HttpResponse("testtt")

def add_game(request):
    result = Game(name="Pierwsza gra",
    person_count=2,
    is_online=False,
    add_date=datetime.datetime.now()
    )
    result.save()
    return HttpResponse("ok")

def get_game(request):
    result = Game.objects.all()
    return HttpResponse(result)

def delete_game(request):
    try:
        result = Game.objects.get(name="Pierwsza gra").delete()
    except Game.DoesNotExist:
        return HttpResponse("Not Found")
    else:
        result = get_object_or_404(Game, name="Pierwsza gra").delete()
        return HttpResponse("deleted")