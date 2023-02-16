import datetime
from pprint import pprint

from django.core.serializers import serialize
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Game, Meeting, Participant
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
                      accepted_by_id=get_object_or_404(User, id=request.POST.get('accepted_by_id')),
                      description=request.POST.get('description'),
                      last_update_date=now(),
                      requested_by_id=get_object_or_404(User, id=request.POST.get('requested_by_id')),
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
        response = JsonResponse(
            {'text': 'added',
             'status': 'success'}
        )
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        return HttpResponse(e)

def add_meeting(request):
    try:
        meeting = Meeting(name=request.POST.get('name'),
                      add_date=now(),
                      game_id=get_object_or_404(Game, id=request.POST.get('game_id')),
                      owner_id=get_object_or_404(User, id=request.POST.get('user_id')),
                      meeting_date=now(),
                      )
        meeting.save()
    except Exception as e:
        return HttpResponse(e)
    return HttpResponse('Meeting added')


def get_game(request):
    result = Game.objects.all()

    data = serialize('json', list(result))
    response = JsonResponse(
        {'data': data}
    )
    response["Access-Control-Allow-Origin"] = "*"
    print(response)
    return response



def get_game_by_id(request):
    result = Game.objects.filter(id=request.GET.get('id')).values()
    response = JsonResponse(
        {'data': list(result)}
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_game_by_status(request):
    result = Game.objects.filter(status=request.GET.get('value'))
    print(result)
    data = serialize('json', list(result))
    response = JsonResponse(
        {'data': data}
    )
    response["Access-Control-Allow-Origin"] = "*"
    print(response)
    return response

def get_user_by_id(request):
    result = User.objects.filter(id=request.POST.get('id')).values()
    response = JsonResponse(
        {'data': list(result)}
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_users(request):
    result = User.objects.values()
    response = JsonResponse(
        {'data': list(result)}
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_meeting_by_id(request):
    result = Meeting.objects.filter(id=request.GET.get('id')).values()
    response = JsonResponse(
        {'data': list(result)}
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_meeting(request):
    result = Meeting.objects.all()

    data = serialize('json', list(result))
    response = JsonResponse(
        {'data': data}
    )
    response["Access-Control-Allow-Origin"] = "*"
    print(response)
    return response

def get_meeting_by_user_id(request):
    result = Meeting.objects.filter(owner_id=request.GET.get('id'))

    data = serialize('json', list(result))
    response = JsonResponse(
        {'data': data}
    )
    response["Access-Control-Allow-Origin"] = "*"
    print(response)
    return response

def add_user_to_meeting(request):
    try:
        user = get_object_or_404(User, id=request.POST.get('user_id'))
        meeting = get_object_or_404(Meeting, id=request.POST.get('meeting_id'))
        meeting.participants_id.add(user)
        meeting.save()
        return HttpResponse("Added user to meeting")

    except User.DoesNotExist or Meeting.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)
def remove_user_from_meeting(request):
    try:
        user = get_object_or_404(User, id=request.POST.get('user_id'))
        meeting = get_object_or_404(Meeting, id=request.POST.get('meeting_id'))
        get_object_or_404(Participant,
                             meeting_id=request.POST.get('meeting_id'),
                             user_id=request.POST.get('user_id'))
        meeting.participants_id.remove(user)
        meeting.save()
        return HttpResponse("Removed user from meeting")
    except get_object_or_404(Participant,
                             meeting_id=request.POST.get('meeting_id'),
                             user_id=request.POST.get('user_id')):
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)
@login_required()
def update_game(request):
    return HttpResponse("Update Game endpoint in preparation")


@login_required()
def delete_game(request):
    try:
        result = Game.objects.filter(id=request.POST.get('id')).delete()
        return HttpResponse("deleted")
    except Game.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)

@login_required()
def delete_user(request):
    try:
        result = User.objects.filter(id=request.POST.get('id')).delete()
        return HttpResponse("User deleted")
    except User.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)

@login_required()
def delete_meeting(request):
    try:
        result = Meeting.objects.filter(id=request.POST.get('id')).delete()
        return HttpResponse("deleted")
    except Meeting.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)

@login_required()
def add_preffered_date(request):
    try:
        preffered_date = request.POST.get('preffered_date')
        result = get_object_or_404(Participant, user_id=request.POST.get('user_id'), meeting_id=request.POST.get('meeting_id'))
        result.prefered_date = preffered_date
        result.save()
        update_suggested_date(meeting_id=request.POST.get('meeting_id'))
        return HttpResponse("Added prefered dates")
    #except request.POST.get('user_id') is None or\
    #       request.POST.get('meeting_id') is None or\
    #       request.POST.get('prefered_date') is None:
    #    return HttpResponse("Invalid Parameters")
    except Exception as e:
        return HttpResponse(e)


def update_suggested_date(meeting_id):
    suggested_date = None
    first_len = 0
    tmp = []
    meeting = get_object_or_404(Meeting, id=meeting_id)
    all_users_prefered_dates = []
    for dates in list(Participant.objects.filter(meeting_id=meeting_id).values('prefered_date')):
        if first_len == 0:
            first_len = len(dates['prefered_date'].split(','))
            tmp.append(dates['prefered_date'].split(','))
        all_users_prefered_dates.append(dates['prefered_date'].split(','))
    tmp = tmp[0]
    #for date in all_users_prefered_dates[first_len:]:
    for user_dates in all_users_prefered_dates[1:]:
        for potential_date in tmp:
            if potential_date not in user_dates:
                tmp.remove(potential_date)

    if len(tmp) > 0:
        suggested_date = tmp[0]
    meeting.meeting_date = suggested_date
    meeting.save()

def auth(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    # return HttpResponse(f"{username}, {password}")
    user = authenticate(request, username=username, password=password)

    if user.is_superuser:
        role = 'admin'
    elif user.is_staff:
        role = 'moderator'
    else:
        role = 'user'
    response = JsonResponse(
        {
            'username': username,
            'role': role,
            'user_id': user.id
        }
    )
    response["Access-Control-Allow-Origin"] = "*"
    if user is not None:
        # response = serialize("json", user, fields=(username, password))
        login(request, user)
        return response
    else:
        return response


def logout(request):
    logout(request)
    return HttpResponse("Logged out")
def permission_denied(request):
    return HttpResponse("Not authorized")
