# coding=utf
"""
author=Hui_T
"""
import datetime
s = datetime.datetime.strftime(datetime.datetime.now(),'%Y-%m/%d')
print(s,type(s))
s2 = datetime.datetime.now().strftime('%Y-%m/%d')
print(s2,type(s2))