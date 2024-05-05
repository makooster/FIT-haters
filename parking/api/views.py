from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse, Http404
import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.models import Users
from .models import parking_center, parking_place, parking_places, street_parking
from .serializers import CenterSerializer, PlaceSerializer, PlacesSerializer, StreetSerializer

@api_view(['GET', 'POST', 'DELETE'])
def user(request):
    if request.method == 'GET':
        accounts = Users.objects.all()
        accounts_json = [account.to_json() for account in accounts]
        return JsonResponse(accounts_json, safe=False)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        id = data.get('id')  
        account = Users.objects.create(
            id=id,
            nickname=data.get('name', ''),
            mail=data.get('mail', ''),
            password = data.get('password', '')
        )
        return JsonResponse(account.to_json())
    if request.method == 'DELETE':
        users = Users.objects.get(pk = id)
        users.delete()
        return Response('User successfully deleted!')


@api_view(['GET'])
def parkingList(request):
    parkings = parking_center.objects.all()
    serializer = PlacesSerializer(parkings, many = True)
    return Response(serializer.data)

@api_view(['GET'])
def parkingListDetail(request, id):
    parkings = parking_places.objects.get(pk = id)
    serializer = CenterSerializer(parkings, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def parkingPlaceDetail(request, id):
    parkings = parking_place.objects.get(pk = id)
    serializer = CenterSerializer(parkings, many = False)
    return Response(serializer.data)

@api_view(['GET'])
def streetIntersection(request):
    intersections = street_parking.objects.all()
    serializer = StreetSerializer(intersections, many = True)
    return Response(serializer.data)

@api_view(['PUT'])
def UpdateParkingInfo(request):
    serializer = PlacesSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PUT'])
def UpdateStreetParkingInfo(request):
    serializer = StreetSerializer(data = request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

