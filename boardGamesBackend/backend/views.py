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
from django.utils.timezone import now
import json


# Create your views here.

def index(request):
    return HttpResponse("index")


@login_required
def add_game(request):
    try:
        result = Game(name=request.POST.get('name'),
                      person_count=request.POST.get('person_count'),
                      is_online=request.POST.get('is_online'),
                      add_date=now(),
                      accept_date=now(),
                      accepted_by_id=2,
                      description=request.POST.get('description'),
                      last_update_date=now(),
                      requested_by_id=request.POST.get('requested_by_id'),
                      status=0,
                      url=request.POST.get('url')
                      )
        result.save()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse("ok")

def add_user(request):
    try:
        user = User.objects.create_user(request.POST.get('username'),
                                        request.POST.get('email'),
                                        request.POST.get('password')
                                       )
        user.save()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('ok')

def add_meeting(request):
    try:
        meeting = Meeting(name=request.POST.get('name'),
                      is_online=request.POST.get('is_online'),
                      add_date=now(),
                      game_id=1,
                      owner_id=2,
                      meeting_date=now(),
                      )
        meeting.save()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('ok')

@login_required()
def get_game(request):
    result = Game.objects.all()
    return result



def get_game_by_id(request):
    result = Game.objects.filter(id=request.GET.get('id'))
    return result

def get_user_by_id(request):
    result = User.objects.filter(id=request.GET.get('id'))
    return result

def get_users(request):
    result = User.objects.all()
    return result

def get_meeting_by_id(request):
    result = Meeting.objects.filter(id=request.GET.get('id'))
    return result

def get_meeting(request):
    result = Meeting.objects.all()
    return result
def add_user_to_meeting(request):
    try:
        user = User.objects.filter(id=request.GET.get('user_id'))
        meeting = Meeting.objects.filter(id=request.GET.get('meeting_id'))
        meeting.participants.add(user)
        meeting.save()
        return HttpResponse("Added user to meeting")

    except User.DoesNotExist or Meeting.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)
def remove_user_from_meeting(request):
    try:
        user = User.objects.filter(id=request.GET.get('user_id'))
        meeting = Meeting.objects.filter(id=request.GET.get('meeting_id'))
        meeting.participants.remove(user)
        meeting.save()
        return HttpResponse("Removed user from meeting")

    except User.DoesNotExist or Meeting.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)
@login_required()
def update_game(request):
    return HttpResponse("Update Game endpoint in preparation")


@login_required()
def delete_game(request):
    try:
        result = Game.objects.filter(id=request.GET.get('id')).delete()
        return HttpResponse("deleted")
    except Game.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)

@login_required()
def delete_user(request):
    try:
        result = User.objects.filter(id=request.GET.get('id')).delete()
        return HttpResponse("deleted")
    except User.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)

@login_required()
def delete_meeting(request):
    try:
        result = Meeting.objects.filter(id=request.GET.get('id')).delete()
        return HttpResponse("deleted")
    except Meeting.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)

def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # return HttpResponse(f"{username}, {password}")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        # response = serialize("json", user, fields=(username, password))
        login(request, user)
        return HttpResponse("authorized")
    else:
        return HttpResponse("Bad credentials")

def logout(request):
    logout(request)
    return HttpResponse("Logged out")
def permission_denied(request):
    return HttpResponse("Not authorized")
