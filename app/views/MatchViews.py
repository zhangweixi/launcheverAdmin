from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

from app.controllers.MatchController import MatchController
from app.models.MatchModel import MatchModel
from app.models.models import Match
from app.models.DB import DB
from common import app



def parse_match_data(request):


    matchId     = request.GET['matchId']
    userId      = request.GET['userId']

    matchController = MatchController(matchId,userId)
    result = matchController.handle()
    #return HttpResponse(result)
    return JsonResponse(result,safe=False)


from app.controllers.CourtController import Point,Court


def init_court_data(request):

    # 业务逻辑开始
    courtId = request.GET['courtId']

    court = Court()

    #初始化球场大小及个点
    #court.init_court_boxs(courtId)

    #测试找到某个点


    # court.draw_point(p.lat,p.lon,'pink')

    #对于热点图的查找应该是遍历大集合，然后在其中遍历所有中心点，对应的中心点数量加一






    p = Point("121.535995,31.320463")
    p.lat = p.lat/p.scale
    p.lon = p.lon/p.scale

    datalist = []
    centerPoints = []

    court.ready_box_points(courtId)

    centerPoint = court.find_which_box(p)
    print(centerPoint)
    #print(centerPoint.lat,centerPoint.lon)




    return HttpResponse('ok')
