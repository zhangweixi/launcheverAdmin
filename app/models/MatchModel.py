import MySQLdb
from django.db import models
from django.db import connection



class MatchModel():

    def __init__(self):

        self.cursor = connection.cursor()


    #获取比赛信息
    def get_match_info(self,matchId):


        sql = "SELECT * FROM users"

        self.cursor.execute(sql)
        users = self.cursor.fetchall()

        return users







