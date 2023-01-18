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
    accepted_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="accepted_by")
    requested_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name="requested_by")
    url = models.URLField()
    description = models.CharField(max_length=100)
    person_count = models.IntegerField()
    is_online = models.BooleanField()

    def __str__(self):
        return f"{self.name}"

class Meeting(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="owner")
    game = models.ForeignKey(Game, on_delete=models.CASCADE, related_name="game")
    participants = models.ManyToManyField(User)
    name = models.CharField(max_length=20)
    add_date = models.DateTimeField(default=timezone.now)
    meeting_date = models.DateTimeField(default=timezone.now)
