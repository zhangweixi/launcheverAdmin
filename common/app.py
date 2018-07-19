import os,sys
import time
import random



def apppath(path=''):
    """
    获得一个文件的绝对路径
    """
    return  os.path.dirname(os.path.dirname(__file__))+"/"+path



def random_str(randomlength=16):
    """
    生成一个指定长度的随机字符串
    """
    random_str = ''
    base_str = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    length = len(base_str) - 1
    for i in range(randomlength):
        random_str += base_str[random.randint(0, length)]
    return random_str
