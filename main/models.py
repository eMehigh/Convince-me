from django.db import models

# Create your models here.
class Room(models.Model):
    room_name = models.CharField(max_length = 20)
    pair_name = models.CharField(max_length = 20, blank = True)
    has_pair = models.BooleanField(default = False)
    pair_left = models.BooleanField(default = False)
    creator_left = models.BooleanField(default = False)
    created = models.BooleanField(default = False)

    def __str__(self):
        return self.room_name
    
class CreatorMessages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank = True, null = True)
    message = models.CharField(max_length=256, blank = True, null = True)

class JoinerMessages(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, blank = True, null = True)
    message = models.CharField(max_length=256, blank = True, null = True)
