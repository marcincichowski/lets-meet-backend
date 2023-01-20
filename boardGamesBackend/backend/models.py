import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    id = models.AutoField(primary_key=True)
    status = models.IntegerField(default=0)
    name = models.CharField(max_length=20)
    add_date = models.DateTimeField(default=timezone.now)
    accept_date = models.DateTimeField(default=timezone.now)
    last_update_date = models.DateTimeField(default=timezone.now)
    accepted_by_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accepted_by")
    requested_by_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requested_by")
    url = models.URLField()
    description = models.CharField(max_length=100)
    person_count = models.IntegerField()
    is_online = models.BooleanField()

    #def __str__(self):
    #    return f"{self.name}"

class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    owner_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    game_id = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")
    participants_id = models.ManyToManyField(User, through='Participant', related_name='participants_id')
    name = models.CharField(max_length=20)
    add_date = models.DateTimeField(default=timezone.now)
    meeting_date = models.CharField(max_length=40, blank=True, null=True)

class Participant(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id")
    meeting_id = models.ForeignKey(Meeting, on_delete=models.CASCADE, related_name="meeting_id")
    prefered_date = models.CharField(max_length=300, blank=True, null=True)