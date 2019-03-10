# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import os
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
import time
import random


url = 'https://rate.bot.com.tw/twd/'
day='2019-03-09'
Deposits_data=[]
startday=['2019','03','09']

while int(startday[0])>1992 :
    print('1')
    try:
        resp = requests.get(url+day)
        resp.encoding = 'utf-8'
        soup = BeautifulSoup(resp.text, 'lxml')
        print('2')


        startday_table = soup.find('div', attrs={'class': 'pull-right trailer pull-left--xs text-info'})
        subtable = soup.find('table', attrs={'class': "table table-bordered table-condensed table-hover toggle-circle table--save twd-table2-style"})
        DD = subtable .find('td', attrs={'colspan': "5"})
    #        CD13 = soup.find('td', attrs={'class': 'footable-visible footable-last-column'})
    #        CD36 = soup.find('td', attrs={'class': 'footable-visible footable-last-column'})
    #        CD69 = soup.find('td', attrs={'class': 'footable-visible footable-last-column'})
    #        CD912 = soup.find('td', attrs={'class': 'footable-visible footable-last-column'})
    #        CD1224 = soup.find('td', attrs={'class': 'footable-visible footable-last-column'})
    #        CD2436 = soup.find('td', attrs={'class': 'footable-visible footable-last-column'})
    #        CD36 = soup.find('td', attrs={'class': 'footable-visible footable-last-column'})


        print('3')


        pattern = re.compile(r'\d+')   # 查找数字
        startday = pattern.findall(startday_table.text)
        print(type(startday))
        print(startday)

        Deposits_data.append([int(startday[0]), int(startday[1]), int(startday[2]), float(DD.text)] )

        day = get_yesterday_date(startday)
        print(day)
        day = str(day[0])+'-'+str(day[1]).zfill(2)+'-'+str(day[2]).zfill(2)

        print('5')

        time.sleep(random.random()*5)


    except :
#        print(Deposits_data)
        break

#print(Deposits_data)
df=pd.DataFrame(Deposits_data,columns=['year', 'month', 'date', 'rate'])
df.to_csv('Demand_Deposits.csv',index=False)

def get_yesterday_date(date):
    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    if day > 1:
        day -= 1
        return [year, month, day]
    else:
#         day = 1
#         if month == 12:
#             month = 1
#             year += 1
#         else:
#             month += 1
        lastyear = year-1
        if (year % 400 == 0):
            leap_year = True
        elif (year % 100 == 0):
            leap_year = False
        elif (year % 4 == 0):
            leap_year = True
        else:
            leap_year = False

        
        if month == 1:
            lastmonth = 12           
            lastday = 31
            return [lastyear, lastmonth, lastday]
        else:
            lastmonth = month-1

            if lastmonth in (1, 3, 5, 7, 8, 10):
                lastday = 31
                return [year, lastmonth, lastday]
            elif lastmonth == 2:
                if leap_year:
                    lastday = 29
                    return [year, lastmonth, lastday]
                else:
                    lastday = 28
                    return [lastyear, lastmonth, lastday]
            else:
                lastday = 30
                return [year, lastmonth, lastday]