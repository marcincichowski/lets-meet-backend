import datetime

from django.db import models

# Create your models here.
class Game(models.Model):
    name = models.CharField(max_length=20)
    person_count = models.IntegerField()
    is_online = models.BooleanField()
    add_date = models.DateTimeField()

    def __str__(self):
        return f"{self.name}"

class Meeting(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    add_date = models.DateTimeField()
    meeting_date = models.DateTimeField(default=datetime.datetime.now())
