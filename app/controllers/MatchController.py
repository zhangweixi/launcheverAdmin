# coding:utf-8
import sys
import time
import json
from win32com.client import Dispatch
import pythoncom

from app.models.DB import DB
from common import app

'''
开始处理数据
1.从数据库提取数据组织成json文件
2.调用matlb系统
3.matlab将结果存入文件
4.python从结果中读取数据，分别存入数据库
'''
class MatchController():

    matchId = 0
    userId = 0


    matlabApp = ""

    def __init__(self,matchId,userId):

        self.matchId = matchId
        self.userId = userId

        pythoncom.CoInitialize()





    def get_matlab_app(self):

        if self.matlabApp == '':

            self.matlabApp = Dispatch('Matlab.application')

        return self.matlabApp


    #程序处理入口
    def handle(self):


        # 获得比赛的开始时间和结束时间
        sql = "SELECT * FROM `match` WHERE match_id =  {self.matchId}"
        sql = sql.format_map(vars())

        matchInfo = DB().one(sql)
        beginTime = str(matchInfo['time_begin'])
        beginTime = time.strptime(beginTime, "%Y-%m-%d %H:%M:%S")
        beginTime = int(time.mktime(beginTime)) * 1000


        matchEndTime = str(matchInfo['time_end'])
        matchEndTime = time.strptime(matchEndTime, "%Y-%m-%d %H:%M:%S")
        matchEndTime = int(time.mktime(matchEndTime)) * 1000

        # 从此开始循坏，不断的获取数据并提供给matlab来处理

        # 暂时
        beginTime = 1527581549164
        endTime = 1527581562424

        fileIndex = 1

        #循坏遍历出本次比赛的所有数据
        while True:
            endTime = beginTime + 6 * 1000  # 时间切片 1分钟 60S
            resultData = self.get_data(beginTime, endTime)

            # if (len(data) == 0 and beginTime >= matchEndTime):
            if resultData == False:  # 退出需要两个条件 1：获取的条数为0 二开始时间已经大于结束时间

                break

            jsonstr = json.dumps(resultData)
            filebase = app.apppath("static/match/json/" + str(self.matchId) + "-" + str(fileIndex))

            sourcefile = filebase + ".json"
            resultfile = filebase + "-1.json"

            file = open(sourcefile, 'w')
            file.write(jsonstr)
            file.close()

            # 调用matlab
            self.call_matlab(sourcefile, resultfile)


            # 更改下一轮的查询变量
            fileIndex = fileIndex + 1

            beginTime = endTime


    #从数据库获数据 并组织成特定的格式
    #Input : beginTime 开始时间
    #Input : endTime 结束时间
    def get_data(self, beginTime, endTime):

        tableGps = "user_" + str(self.userId) + "_gps"
        tableSensor = "user_" + str(self.userId) + "_sensor"
        beginTime = str(beginTime)
        endTime = str(endTime)

        hasData = False

        ax = []
        ay = []
        az = []
        gx = []
        gy = []
        gz = []
        lat = []
        lon = []

        # 按时间切面来获取数据

        # ==================获取sensor数据=================
        #
        sensorSql = "SELECT * FROM {tableSensor} where match_id =  {self.matchId} AND   `timestamp` > {beginTime} AND `timestamp` < {endTime} order by id "
        sensorSql = sensorSql.format_map(vars())

        sensorList = DB().all(sensorSql,'dbmatch')

        if sensorList!= None:

            hasData = True

        if sensorList != None:
            for sensor in sensorList:

                dataType = sensor['type']

                if dataType == 'A':

                    ax.append(sensor['x'])
                    ay.append(sensor['y'])
                    az.append(sensor['z'])

                elif dataType == 'G':

                    gx.append(sensor['x'])
                    gy.append(sensor['y'])
                    gz.append(sensor['z'])

                else:

                    pass

        # ===================获取gps数据===================
        #
        gpsSql = 'SELECT * FROM {tableGps} WHERE match_id =  {self.matchId}  AND   `timestamp` > {beginTime} AND `timestamp` < {endTime} order by id '

        gpsSql = gpsSql.format_map(vars())

        gpsList = DB().all(gpsSql,'dbmatch')

        if hasData == False and gpsList != None:
            hasData = True

        if gpsList != None:
            for gps in gpsList:
                lat.append(gps.latitude)
                lon.append(gps.longitude)


        if hasData == True:

            data = {'ax': ax, 'ay': ay, 'az': az, 'gx': gx, 'gy': gy, 'gz': gz, 'lat': lat, 'lon': lon}
            return data

        else:

            return False


    #调用matlab
    #Input : sourcefile    需要用于计算的数据文件
    #Input : resultfile    结果保存的文件
    def call_matlab(self, sourcefile, resultfile):

        sourcefile = sourcefile.replace('\\','/')
        resultfile = resultfile.replace('\\','/')
        # 1.切换工作目录
        workplacedir = app.apppath('static/matlab')

        self.get_matlab_app().execute("cd " + workplacedir)

        # 2.添加matlab脚本所在的目录到路径中

        self.get_matlab_app().execute("addpath('" + workplacedir + "')")


        # 3.调用函数
        command = "beike('{sourcefile}','{resultfile}')".format_map(vars())
        result = self.get_matlab_app().execute(command)

        print(result)

    '''
    #保存结果    
    '''

    def save_result(self):

        # 得到的结果应该达到这样的目的 用户在什么时间，什么地址，完成了什么样的功能

        pass




