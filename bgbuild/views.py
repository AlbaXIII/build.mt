from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bgbuildtest(request):
    return HttpResponse("Port Operational")