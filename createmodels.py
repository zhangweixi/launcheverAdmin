#coding:utf-8
import os
import re

rootpath   = os.path.dirname(os.path.abspath(__file__))
mangerfile = rootpath + "/manage.py"
tempfile   = rootpath + "/temp.py"
tempfilePath=tempfile


command = "python "+mangerfile + " inspectdb > " + tempfile
result = os.system( command )



tempfile    = open(tempfile,'r+')
modelsfile  = rootpath + "/matlab/models.py"
modelsfile  = open(modelsfile,'w')


for line in tempfile:

    if re.search('from',line):
        modelsfile.writelines("from . import mymodels\n")

    if re.search("(models.Model)",line):
        line = re.sub("\(models\.Model\)","(models.Model,mymodels.mymodels)",line)

    modelsfile.writelines(line)



modelsfile.close()
tempfile.close()

os.remove(tempfilePath)


print('模型创建成功')

