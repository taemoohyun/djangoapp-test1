from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
import random

# Create your views here.



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