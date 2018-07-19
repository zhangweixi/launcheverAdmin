from common.apiData import ApiData
from django.http import HttpResponse
from matlab import models
import hashlib
import datetime
import time
from common.app import *


def login(request):
    '''
    登录
    :param request:
    :return:
    '''
    name = request.POST.get('name','')
    pswd = request.POST.get('password','')
    pswd = get_password(pswd)


    try:
        adminInfo = models.Admin.objects.filter(name=name).filter(password=pswd).get()

    except models.Admin.DoesNotExist:

        adminInfo = None


    if adminInfo == None:

        return ApiData().send(2001,"登录失败")

    #刷新token

    adminInfo.token = random_str(30)
    adminInfo.save()

    adminInfo = adminInfo.toJSON()

    return ApiData().add('adminInfo',adminInfo).add('name',name).send()




def get_admin_info_by_token(request):
    """
    根据token获取管理员信息
    :param request:
    :return:
    """
    token = request.GET.get('token','')

    try:
        adminInfo = models.Admin.objects.filter(token=token).get()

    except models.Admin.DoesNotExist:

        adminInfo = None

    if adminInfo == None:
        return ApiData().send(2001,'管理员不存在')


    adminInfo = adminInfo.toJSON()

    return ApiData().add('admin',adminInfo).send()


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


