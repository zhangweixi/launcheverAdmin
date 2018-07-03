import MySQLdb
from django.db import models
from django.db import connection,connections




def singleton(cls):
    instances = {}

    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]

    return wrapper


@singleton
class DB():

    dbbase = connection.cursor()
    dbmatch= connections['dbmatch'].cursor()
    dbs = {}


    def __init__(self):

        self.dbs['dbbase'] = self.dbbase
        self.dbs['dbmatch'] = self.dbmatch


    #更新数据
    def update(self,sql,db='dbbase'):

        return self.dbs[db].execute(sql)


    #插入数据
    def insert(self,sql,db='dbbase'):
        return self.dbs[db].execute(sql)




    def one(self,sql,db='dbbase'):

        info = self.exec(sql,db)
        infolength = len(info)
        if infolength > 0:
            info = info[0]
        else:
            info = None

        return info


    def all(self,sql,db='dbbase'):

        info = self.exec(sql, db)
        infolength = len(info)
        if infolength == 0:
            info = None
        return info


    def exec(self,sql,db):

        db = self.dbs[db]
        db.execute(sql)

        #info = db.fetchall()

        info = self.dictfetchall(db)
        return info


    #组合成字典的形式
    def dictfetchall(self,cursor):
        "将游标返回的结果保存到一个字典对象中"
        desc = cursor.description
        return [
            dict(zip([col[0] for col in desc], row))
            for row in cursor.fetchall()
        ]
