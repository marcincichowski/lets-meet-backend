from rest_framework import viewsets
from .serializers import UserSerializer, GameSerializer, MeetingSerializer, ParticipantSerializer, \
    WriteMeetingSerializer
from django.contrib.auth.models import User
from .models import Game, Meeting, Participant


class UserViewSet(viewsets.ModelViewSet):

    serializer_class = UserSerializer
    queryset = User.objects.all()


class GameViewSet(viewsets.ModelViewSet):

    serializer_class = GameSerializer
    queryset = Game.objects.all()


class MeetingViewSet(viewsets.ModelViewSet):
    serializer_class = WriteMeetingSerializer
    queryset = Meeting.objects.all()

    def get_serializer_class(self):
        if self.action == "list" or self.action == "retrieve":
            return MeetingSerializer
        else:
            return WriteMeetingSerializer

class ParticipantViewSet(viewsets.ModelViewSet):

    serializer_class = ParticipantSerializer
    queryset = Participant.objects.all()
