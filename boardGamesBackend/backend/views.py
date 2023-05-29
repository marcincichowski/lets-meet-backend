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
        response = HttpResponse(e)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    response = HttpResponse('success')
    response["Access-Control-Allow-Origin"] = "*"
    return response

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
        response = HttpResponse(e)
        response["Access-Control-Allow-Origin"] = "*"
        return response
    response = HttpResponse('success')
    response["Access-Control-Allow-Origin"] = "*"
    return response


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
    data = serialize('json', Game.objects.filter(id=request.GET.get('id')))
    print(data)
    response = JsonResponse(
        {'data': data}
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
    test = User.objects.values()
    test2 = list(test)
    print(test2)
    data = serialize('json', User.objects.filter(id=request.GET.get('id')), fields=['id', 'password'])
    #print(data)
    response_data = json.loads(data)
    #print(response_data)
    response = HttpResponse(
        {'data': data}
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
    result = serialize('json', Meeting.objects.filter(id=request.GET.get('id')))
    response = JsonResponse(
        {'data': result}
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

def get_meeting(request):
    data = serialize('json', Meeting.objects.all(), use_natural_primary_keys=True, use_natural_foreign_keys=True)
    #pprint(data)
    response = JsonResponse(
        {'data': data}
    )
    print(data)
    response["Access-Control-Allow-Origin"] = "*"
    print(response)
    return response

def meeting_get_users(request):
    data = serialize('json', Participant.objects.filter(meeting_id_id=request.GET.get('id')), use_natural_primary_keys=True, use_natural_foreign_keys=True)
    response = JsonResponse(
            {'data': data}
    )
    response["Access-Control-Allow-Origin"] = "*"
    print(response)
    return response


def get_meeting_by_user_id(request):
    data = serialize('json', Meeting.objects.filter(owner_id=request.GET.get('id')), use_natural_primary_keys=True, use_natural_foreign_keys=True)
    response = JsonResponse(
        {'data': data}
    )
    response["Access-Control-Allow-Origin"] = "*"
    print(response)
    return response

def add_user_to_meeting(request):
    try:
        print(request.POST.get('user_id'))
        user = get_object_or_404(User, id=request.POST.get('user_id'))
        meeting = get_object_or_404(Meeting, id=request.POST.get('meeting_id'))
        meeting.participants_id.add(user)
        meeting.save()
        response = HttpResponse("Added user to meeting")
        response["Access-Control-Allow-Origin"] = "*"
        return response

    except User.DoesNotExist or Meeting.DoesNotExist:
        response = HttpResponse("Not Found")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        response = HttpResponse(e)
        response["Access-Control-Allow-Origin"] = "*"
        return response

def remove_user_from_meeting(request):
    try:
        result = Participant.objects.filter(user_id=request.GET.get('id'))
        print(result)
        result.delete()
        response = HttpResponse("DELETED")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        print(e)
        response = HttpResponse(e)
        response["Access-Control-Allow-Origin"] = "*"
        return response

@login_required()
def update_game(request):
    return HttpResponse("Update Game endpoint in preparation")

def accept_game(request):
    try:
        result = get_object_or_404(Game, id=request.GET.get('id'))
        result.status = 1
        result.save()
        response = HttpResponse('success')
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        response = HttpResponse(e)
        response["Access-Control-Allow-Origin"] = "*"
        return response

def delete_game(request):
    try:
        result = Game.objects.filter(id=request.GET.get('id')).delete()
        response = HttpResponse('deleted')
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Game.DoesNotExist:
        response = HttpResponse('not found')
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        response = HttpResponse(e)
        response["Access-Control-Allow-Origin"] = "*"
        return response

@login_required()
def delete_user(request):
    try:
        result = User.objects.filter(id=request.POST.get('id')).delete()
        return HttpResponse("User deleted")
    except User.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)

def delete_meeting(request):
    try:
        result = Meeting.objects.filter(id=request.POST.get('id')).delete()
        return HttpResponse("deleted")
    except Meeting.DoesNotExist:
        return HttpResponse("Not Found")
    except Exception as e:
        return HttpResponse(e)

def add_preffered_date(request):
    try:
        preffered_date = request.POST.get('preffered_date')
        splited = preffered_date.split(' ')

        if splited[1] == 'Jan':
            splited[1] = 1
        elif splited[1] == 'Feb':
            splited[1] = 2
        elif splited[1] == 'Mar':
            splited[1] = 3
        elif splited[1] == 'Apr':
            splited[1] = 4
        elif splited[1] == 'May':
            splited[1] = 5
        elif splited[1] == 'Jun':
            splited[1] = 6
        elif splited[1] == 'Jul':
            splited[1] = 7
        elif splited[1] == 'Aug':
            splited[1] = 8
        elif splited[1] == 'Sep':
            splited[1] = 9
        elif splited[1] == 'Oct':
            splited[1] = 10
        elif splited[1] == 'Nov':
            splited[1] = 11
        elif splited[1] == 'Dec':
            splited[1] = 12

        date = datetime.datetime(int(splited[3]), splited[1], int(splited[2]))

        result = get_object_or_404(Participant, user_id=request.POST.get('user_id'), meeting_id=request.POST.get('meeting_id'))
        result.prefered_date = date
        result.save()
        # update_suggested_date(meeting_id=request.POST.get('meeting_id'))

        response = HttpResponse("Added prefered dates")
        response["Access-Control-Allow-Origin"] = "*"
        return response
    #except request.POST.get('user_id') is None or\
    #       request.POST.get('meeting_id') is None or\
    #       request.POST.get('prefered_date') is None:
    #    return HttpResponse("Invalid Parameters")
    except Exception as e:
        response = HttpResponse(e)
        response["Access-Control-Allow-Origin"] = "*"
        return response

def set_meeting_date(request):
    try:
        meeting_id = request.POST.get('meeting_id')
        prefered_date = request.POST.get('prefered_date')

        meeting = Meeting.objects.get(id=meeting_id)
        meeting.meeting_date = prefered_date
        meeting.save()

        response = HttpResponse('saved')
        response["Access-Control-Allow-Origin"] = "*"
        return response
    except Exception as e:
        response = HttpResponse(e)
        response["Access-Control-Allow-Origin"] = "*"
        return response

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
    print(request.content_params)
    print(request.content_type)
    print(request.headers)
    print(request.body)
    username = request.POST.get('username')
    password = request.POST.get('password')
    # return HttpResponse(f"{username}, {password}")
    print(username)
    print(password)
    user = authenticate(request, username=username, password=password)


    if user is not None:
        # response = serialize("json", user, fields=(username, password))
        login(request, user)
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
        return response
    else:
        response = HttpResponse(status=401)
        response["Access-Control-Allow-Origin"] = "*"
        return response


def logout(request):
    logout(request)
    return HttpResponse("Logged out")
def permission_denied(request):
    return HttpResponse("Not authorized")
