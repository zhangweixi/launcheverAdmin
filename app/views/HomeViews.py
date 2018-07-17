from django.http import HttpResponse
from django.http import JsonResponse
import sys

import json
from common.apiData import ApiData



def welcome(request):
    platform = sys.platform
    name = "this is admin,if you don't get the right,please out here right now"

    return HttpResponse(name)



def index(request):

    return HttpResponse("home index")