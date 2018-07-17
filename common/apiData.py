# -*- coding:UTF-8 -*-
from django.http import HttpResponse
from django.http import JsonResponse

class ApiData:

    def __init__(self):

        self.__data = {}


    def add(self,key,value):

        self.__data[key] = value
        return self



    def send(self, code=200, message="SUCCESS"):

        data = {"code":code,"msg":message,"data":self.__data}
        return JsonResponse(data,safe=False)
