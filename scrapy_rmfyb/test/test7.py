# coding=utf
"""
author=Hui_T
"""
import datetime
# now = datetime.datetime.now()
# print(now,type(now))
# now2 = datetime.datetime.strptime("2010-01-01",'%Y-%m-%d')
# print(now2,type(now2))

now = datetime.datetime.now()
start = datetime.datetime.strptime("2010-01/01",'%Y-%m/%d')
one_day = datetime.timedelta(days=1)
while start<=now:
    print(start.strftime("%Y-%m/%d"))
    start+= one_day
