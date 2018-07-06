from django.http import HttpResponse
import sys


def welcome(request):
    platform = sys.platform
    return HttpResponse(platform)



def index(request):

    return HttpResponse("home index")