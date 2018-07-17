from common.apiData import ApiData
from django.http import HttpResponse
from matlab import models
import hashlib
import datetime
import time
import json


def login(request):
    '''
    登录
    :param request:
    :return:
    '''

    name = request.GET['name']
    pswd = request.GET['password']
    pswd = get_password(pswd)


    #adminInfo = models.Admin.objects.filter(name=name).filter(password=pswd).get()
    adminInfo = models.Admin.objects.filter(name=name).filter(password=pswd).values()

    print(adminInfo)

    return ApiData() \
        .add('info',list(adminInfo))\
        .send()







def get_password(password):
    '''
    账户加密
    :param password:
    :return:
    '''

    password = password.encode('utf-8')
    password = hashlib.md5(password).hexdigest()
    password = password.encode('utf-8')
    password = hashlib.sha1(password).hexdigest()

    return password


def add_admin(request):
    '''
    添加管理员
    :param request:
    :return HttpResponse:
    '''

    today = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

    password = "123123"
    password = password.encode('utf-8')
    password = hashlib.md5(password).hexdigest()
    password = hashlib.sha1(password.encode('utf-8')).hexdigest()

    admin = models.Admin()
    admin.password = password
    admin.name = "zhangweixi"
    admin.real_name = "张维喜"
    admin.created_at =today
    admin.updated_at = today
    admin.save()


    return HttpResponse('ok')


