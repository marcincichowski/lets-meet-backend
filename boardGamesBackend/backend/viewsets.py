from rest_framework import viewsets
from .serializers import UserSerializer, GameSerializer, MeetingSerializer, ParticipantSerializer
from django.contrib.auth.models import User
from .models import Game, Meeting, Participant


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class GameViewSet(viewsets.ModelViewSet):

    serializer_class = GameSerializer
    queryset = Game.objects.all()


class MeetingViewSet(viewsets.ModelViewSet):

    serializer_class = MeetingSerializer
    queryset = Meeting.objects.all()


class ParticipantViewSet(viewsets.ModelViewSet):

    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
