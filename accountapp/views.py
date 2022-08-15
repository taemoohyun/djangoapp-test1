from django.contrib.auth.models import User
from django.http import HttpResponse

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import DBTest
from .serializers import DBTestSerializer
import random

# Create your views here.

@api_view(['GET'])
def helloAPI(request):
	return Response("hello world!")

@api_view(['GET'])
def randomDBTest(request,id):
	totalDBTests = DBTest.objects.all()
	randomDBTests = random.samp;le(list(totalDBTests),id)
	serializer = DBTestSerializer(randomDBTests,many=True)
	return Response(serializer.data)

def hello_world(request):
	return HttpResponse('Hello_world!')

def hello_world_mvt(request):
	return render(request, 'accountapp/temp.html')

def test(request):
	msg = 'test message'
	return render(request, 'accountapp/temp.html', {'message':msg})

def test2(request):
	users = User.objects.all()
	context = {
		'users': users,
	}
	return render(request, 'accountapp/temp2.html', context)