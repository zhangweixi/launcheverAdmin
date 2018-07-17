from django.http import HttpResponse
from admin import views

def adminindex(request,module,method):

    MODULE = getattr(views,module,None)
    if MODULE == None:
        message = "模块" + module + "不存在"
        return HttpResponse(message)


    METHOD = getattr(MODULE,method,None)

    if METHOD == None:
        message = "方法" + method + "不存在"

        return HttpResponse(message)

    return METHOD(request)