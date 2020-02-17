#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 13 17:24:15 2020

Inspired by https://xkcd.com/2266/

@author: scottstewart
"""


import time as t

def findTime_2266():
    now = t.localtime()
    year =  (now.tm_year - 2020)*366*24*60*60
    day = (now.tm_yday - 1 - 31)*24*60*60
    hour = (now.tm_hour - 0)*60*60
    minute = (now.tm_min - 0)*60
    second = (now.tm_sec - 0)
    time = (year + day +hour + minute +second) * 1.034
    
    year = int((time - time%(366*24*60*60))/(366*24*60*60) +2020)
    month = int((time - time%(12*24*60*60))/(12*24*60*60) +1)
    day = int((time - time%(24*60*60))/(24*60*60) + 1)
    time = time - (year - 2020)*366*24*60*60
    time = time - (day -1)*24*60*60
    hour = int((time - time%(60*60))/(60*60) + 0)
    time = time - (hour)*60*60
    minute = int((time - time%(60))/(60) + 0)
    
    
    year = "{}".format('%04.0d' % (year))
    month = "{}".format('%02.0d' % (month))
    day =  "{}".format('%02.0d' % (day))
    hour =  "{}".format('%02.0d' % (hour))
    minute =  "{}".format('%02.0d' % (minute))
    
    print(str(year)+"-"+str(month)+"-"+str(day)+"T"+str(hour)+":"+str(minute)) # always use ISO 8601 for simplicity. See: https://xkcd.com/927/

    
    
findTime_2266()