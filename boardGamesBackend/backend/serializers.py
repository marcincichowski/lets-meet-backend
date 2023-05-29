from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Game, Meeting, Participant


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'first_name', 'last_name', 'email', 'is_staff', 'is_active', 'is_superuser']


class UserNestedSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'id']


class GameSerializer(serializers.ModelSerializer):

    class Meta:
        model = Game
        fields = '__all__'


class MeetingSerializer(serializers.ModelSerializer):
    participants_id = UserNestedSerializer(many=True, read_only=True)

    class Meta:
        model = Meeting
        fields = '__all__'


class WriteMeetingSerializer(serializers.ModelSerializer):
    participants_id = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), many=True)

    class Meta:
        model = Meeting
        fields = '__all__'


class ParticipantSerializer(serializers.ModelSerializer):

    class Meta:
        model = Participant
        fields = '__all__'
