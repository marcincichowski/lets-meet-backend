from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

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

    def get_queryset(self):
        queryset = Participant.objects.all()
        meeting = self.request.query_params.get('meeting')
        if meeting is not None:
            queryset = queryset.filter(meeting_id=meeting)
        return queryset

    @action(detail=True, methods=['patch'])
    def set_prefered_date(self, request, pk=None):
        meeting = self.request.query_params.get('meeting')
        user_id = self.request.query_params.get('user_id')
        participant = Participant.objects.get(meeting_id=meeting, user_id=user_id)
        serializer = ParticipantSerializer(data=request.data)
        if serializer.is_valid():
            participant.prefered_date(serializer.validated_data['prefered_date'])
            participant.save()
            return Response({'status': 'date set'})
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
