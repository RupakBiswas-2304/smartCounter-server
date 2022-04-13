from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
import hashlib
import uuid
# Create your views here.
class Index(APIView):
    def get(self, request):
        return render(request, 'index.html')


class Count(APIView):
    def get(self, request):
        id = request.headers['id']
        device = Device.objects.filter(mac_id = id)
        if (device):
            print(device[0].room.present_in)
            return Response({"total_present": device[0].room.present_in})
        else :
            return Response({'message':'Device not found'})
    def post(self, request):
        id = request.headers['id']
        device = Device.objects.filter(mac_id = id)
        if (device):
            count_in = int(request.data['count_in'])
            count_out = int(request.data['count_out'])

            device[0].room.total_in += count_in
            device[0].room.total_out += count_out
            device[0].room.present_in  = device[0].room.total_in - device[0].room.total_out
            device[0].room.save()
            return Response({'total_present': device[0].room.present_in})
        else :
            return Response({'message':'Device not found'})

class Register(APIView):
    def post(self, request):
        name = request.data['name']
        loginID = request.data['username']
        password = request.data['password']
        password = hashlib.md5(password.encode()).hexdigest()
        authtoken = str(uuid.uuid4())
        try :
            house = House.objects.create(
            name=name,
            loginID=loginID,
            password=password,
            total_room=0,
            total_device=0,
            authtoken=authtoken)

            return Response({'message':'Successfully registered', 'authtoken' : authtoken},200)
        except Exception as e :
            print(e)
            return Response({'message':'Server error'}, 500)

class Login(APIView):
    def post(self, request):
        loginID = request.data['username']
        password = request.data['password']
        password = hashlib.md5(password.encode()).hexdigest()
        try :
            house = House.objects.get(loginID=loginID, password=password)
            new_authtoken = str(uuid.uuid4())
            house.authtoken = new_authtoken
            house.save()
            return Response({'message':'Successfully logged in', 'authtoken' : new_authtoken},200)
        except Exception as e :
            return Response({'message':'Invalid credentials'}, 401)

class Rooms(APIView):
    def post(self,request):
        authtoken = request.headers['authtoken']
        house = House.objects.filter(authtoken=authtoken)
        try :
            name = request.data['name']
            try :
                room = Room.objects.create(
                name=name,
                house=house[0],
                total_device=0,
                total_in=0,
                total_out=0,
                present_in=0)
                house[0].total_room += 1
                house[0].save()
                return Response({'message':'Successfully created room'},200)
            except Exception as e :
                print(e)
                return Response({'message':'Server error'}, 500)
        except :
            return Response({'message':'Invalid authtoken'}, 401)
    def get(self,request):
        authtoken = request.headers['authtoken']
        house = House.objects.filter(authtoken=authtoken)
        try :
            rooms = Room.objects.filter(house=house[0])
            return Response({'rooms':[{"name":room.name,"id": room.id, "total-device": room.total_device,"total-in": room.total_in,"total-out" : room.total_out,"present-in": room.present_in} for room in rooms]},200)
        except Exception as e :
            print(e)
            return Response({'message':'Server error'}, 500)
    


class Devices(APIView):
    def post(self, request):
        authtoken = request.headers['authtoken']
        house = House.objects.filter(authtoken=authtoken)
        try :
            mac_id = request.data['mac-id']
            room_id = request.data['room-id']
            try :
                roomx = Room.objects.filter(id=room_id)
                device = Device.objects.create(
                room = roomx[0],
                mac_id = mac_id,
                house = house[0],
                post_url = "null",
                get_url = "null",
                )
                house[0].total_device += 1
                house[0].save()
                roomx[0].total_device += 1
                roomx[0].save()
                return Response({'message':'Successfully created device'},200)
            except Exception as e :
                print(e)
                return Response({'message':'Server error'}, 500)
        except :
            return Response({'message':'Invalid authtoken'}, 401)

    def get(self, request):
        authtoken = request.headers['authtoken']
        house = House.objects.filter(authtoken=authtoken)
        try :
            devices = Device.objects.filter(house=house[0])
            return Response({'devices':[{"mac-id":device.mac_id,"room-id": device.room.id} for device in devices]},200)
        except Exception as e :
            print(e)
            return Response({'message':'Server error'}, 500)