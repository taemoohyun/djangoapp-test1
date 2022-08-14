from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def hello_world(request):
	return HttpResponse('Hello_world!')

def hello_world_mvt(request):
	return render(request, 'accountapp/temp.html')