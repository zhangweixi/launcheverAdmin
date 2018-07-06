#coding:utf-8

import sys
if sys.platform == 'win32':
    from pylab import *
    from numpy import *

from app.models.DB import DB
import json
import math



#一个经纬度坐标点
class Point():
    lat = 0
    lon = 0

    scale = 100000000

    def __init__(self, gps):

        gpsInfo = gps.split(',')

        self.lat = float(gpsInfo[0]) * self.scale
        self.lon = float(gpsInfo[1]) * self.scale



class Court():

    latNum = 10
    lonNum = 10

    points = []
    courtId=0

    a = Point("0,0")
    d = Point("0,0")
    e = Point("0,0")
    f = Point("0,0")
    g = Point("0,0")
    h = Point("0,0")





    #初始化足球场需要的数据
    def init_court_boxs(self,courtId):

        self.courtId = courtId

        self.init_court_points()    #初始化个点

        self.create_full_court()    #创建一个完整的球场

        self.cut_court()            #切分成多个块
        candraw = False

        if candraw:
            self.draw_point(self.a.lat, self.a.lon)
            self.draw_point(self.d.lat, self.d.lon)
            self.draw_point(self.e.lat, self.e.lon, 'black')
            self.draw_point(self.f.lat, self.f.lon)
            self.draw_point(self.g.lat, self.g.lon, 'black')
            self.draw_point(self.h.lat, self.h.lon)

            plt.show()


    # 从数据库提取数据并初始化各个点
    def init_court_points(self):

        sql = "SELECT * FROM football_court WHERE court_id = {0}".format(self.courtId)

        courtInfo = DB().one(sql)
        self.a = Point(courtInfo['p_a'])
        self.d = Point(courtInfo['p_d'])
        self.e = Point(courtInfo['p_e'])
        self.f = Point(courtInfo['p_f'])

        # 创建一个完整的足球场 足球场呈现s型 |_|一|

    def create_full_court(self):

        lat1 = self.f.lat + (self.f.lat - self.a.lat)
        lon1 = self.f.lon + (self.f.lon - self.a.lon)
        lat2 = self.e.lat + (self.e.lat - self.d.lat)
        lon2 = self.e.lon + (self.e.lon - self.d.lon)

        self.g.lat = lat1
        self.g.lon = lon1

        self.h.lat = lat2
        self.h.lon = lon2

        # 存储完整的数据
        pg = str(lat1 / Point.scale) + "," + str(lon1 / Point.scale)
        ph = str(lat2 / Point.scale) + "," + str(lon2 / Point.scale)

        sql = "UPDATE football_court SET p_a1 = '{pg}',p_d1 = '{ph}' WHERE court_id = {id}".format_map(
            {'pg': pg, 'ph': ph, 'id': self.courtId})
        DB().update(sql)

    #切割足球场
    def cut_court(self):

        #先将矩形画成很多矩形
        left = []
        right= []
        middlePoints = []


        #a->d构成一条边  g-h构成一条边

        avg_a_d_lat = (self.d.lat - self.a.lat)/self.lonNum
        avg_a_d_lon = (self.d.lon - self.a.lon)/self.lonNum


        avg_g_h_lat = (self.h.lat - self.g.lat)/self.lonNum
        avg_g_h_lon = (self.h.lon - self.g.lon)/self.lonNum

        # 切分方格，并找到方格的中心点
        for i in range(0,self.lonNum+1):

            leftLat = self.a.lat + i * avg_a_d_lat
            leftLon = self.a.lon + i * avg_a_d_lon
            rightLat= self.g.lat + i * avg_g_h_lat
            rightLon= self.g.lon + i * avg_g_h_lon


            left.append({"lat":leftLat,"lon":leftLon})
            right.append({"lat":rightLat,"lon":rightLon})


            self.draw_point(leftLat,leftLon,'blue')
            self.draw_point(rightLat,rightLon,'blue')

            plt.scatter(leftLat,leftLon, c='red', s=50, alpha=0.4, marker='o')  # 散点图
            plt.scatter(rightLat, rightLon, c='red', s=50, alpha=0.4, marker='o')  # 散点图
            #plt.show()
            #sys.exit()


            # 这里得到左边点和右边点 把两个点链接组成一条线 再切分
            singleLat = (rightLat - leftLat)/self.latNum
            singleLon = (rightLon - rightLon)/self.latNum


            linePoints  = []

            if(i%2 == 1):

                for j in range(0,self.latNum+1):

                    lat = leftLat + j * singleLat
                    lon = leftLon + j * singleLon

                    if j % 2 == 1:

                        #plt.scatter(lat, lon, c='green', s=50, alpha=0.4, marker='o')  # 散点图
                        lat = lat/Point.scale
                        lon = lon/Point.scale

                        linePoints.append({"lat":lat,"lon":lon})

                    else:

                        #plt.scatter(lat, lon, c='red', s=50, alpha=0.4, marker='o')  # 散点图
                        pass

                middlePoints.append(linePoints)

        #将数据存储到数据库
        boxs = json.dumps(middlePoints)
        sql  = "UPDATE football_court SET boxs = '{boxs}' WHERE court_id = {id}".format_map({'boxs':boxs,'id':self.courtId})

        DB().update(sql)

        #print(json.dumps(middlePoints,indent=4))
        self.points = middlePoints


        #print(json.dumps(self.points,indent=4))

        #把数据存储在服务器


    def ready_box_points(self,courtId):

        self.courtId = courtId

        sql = "SELECT boxs FROM football_court WHERE court_id = {id}".format_map({"id":self.courtId})
        courtInfo = DB().one(sql)


        if courtInfo != None:

            boxs = eval(courtInfo['boxs'])
            self.points = boxs

            return boxs

        else:
            return []



    #在图上，其实显示的不是那个经纬度的点，而是那个坐标的点
    #Input : points 要解析的数据列表

    def find_which_box(self,points : Point):


        dis = 1000000000000
        minDisBox = Point("0,0")

        minDisKey = []



        for point in points:

            i1 = 0

            for line in self.points:

                i2 = 0

                for singleBox in line:



                    newDis = (point.lat - singleBox["lat"]) ** 2 + (point.lon - singleBox["lon"]) ** 2


                    if newDis < dis :

                        dis = newDis
                        #minDisBox.lat = singleBox['lat']
                        #minDisBox.lon = singleBox['lon']

                        minDisKey = [i1,i2]

                    i2 = i2 + 1
                i1 = i1 + 1





        #self.draw_point(minDisBox.lat,minDisBox.lon,'red')


    #绘制一个圆形
    def draw_point(self,lat,lon,c='red'):

        plt.scatter(lat, lon, c=c, s=50, alpha=0.4, marker='o')  # 散点图











