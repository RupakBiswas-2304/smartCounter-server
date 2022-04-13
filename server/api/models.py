from statistics import mode
from django.db import models

# Create your models here.
class House(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    loginID = models.CharField(max_length=100, unique= True)
    password = models.CharField(max_length=100)
    total_room = models.IntegerField(default= 0)
    total_device = models.IntegerField(default= 0)
    authtoken = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Room(models.Model):
    name = models.CharField(max_length=100)
    id = models.AutoField(primary_key=True)
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    total_device = models.IntegerField(default = 0)
    total_in = models.IntegerField(default= 0)
    total_out = models.IntegerField(default= 0)
    present_in = models.IntegerField(default= 0)

    def __str__(self):
        return str(self.name)

class Device(models.Model):
    id = models.AutoField(primary_key=True)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    house = models.ForeignKey(House, on_delete=models.CASCADE, null = True)
    mac_id = models.CharField(max_length=100, unique= True)
    post_url = models.CharField(max_length=300)
    get_url = models.CharField(max_length=300)

    def __str__(self):
        return self.mac_id

