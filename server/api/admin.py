from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(House)
class HouseAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'loginID', 'password', 'total_room', 'total_device')
    # search_fields = ('name', 'id', 'loginID', 'password', 'total_room', 'total_device')
    list_filter = ('name', 'id', 'loginID', 'password', 'total_room', 'total_device')

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'house', 'total_device', 'total_in', 'total_out', 'present_in')
    # search_fields = ('name', 'id', 'house', 'total_device', 'total_in', 'total_out', 'present_in')
    list_filter = ('name', 'id', 'house', 'total_device', 'total_in', 'total_out', 'present_in')

@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ('id', 'room', 'mac_id' )
    # search_fields = ('id', 'room', 'mac_id')
    list_filter = ('id', 'room', 'mac_id')