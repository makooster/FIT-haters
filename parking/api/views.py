from django.shortcuts import render
from rest_framework.views import APIView
from django.http.response import JsonResponse, Http404
import json
from rest_framework.decorators import api_view
from api.models import Users

@api_view(['GET', 'POST'])
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
