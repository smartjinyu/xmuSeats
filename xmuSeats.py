#!usr/bin/python
# -*- coding=utf-8 -*-

#this py is used to collect seats information in Xiamen University Library
__author__ = 'smartjinyu'
import requests
from bs4 import BeautifulSoup
import sqlite3
import time


def parse():
    url = 'http://library.xmu.edu.cn/portal/seatmanage.asp'
    try:
        session = requests.get(url)
        soup = BeautifulSoup(session.content, 'lxml')
        seatList_soup = soup.find('ul', attrs={'class', 'SeatRoom'})
        for room in seatList_soup.find_all('li'):
            # room = <li class="rb close" id="roomstate1"><p class="RoomName">书库1楼</p><p><span class="st" id="st1">0</span>/<span class="sa" id="sa1">13</span></p></li>
            curTime = time.time()
            tableName = room['id']
            roomName = room.find('p',attrs={'class', 'RoomName'}).getText()
            used = int(room.find('span',attrs={'class', 'st'}).getText())
            total = int(room.find('span',attrs={'class', 'sa'}).getText())
            conn = sqlite3.connect('seatState.db')
            cursor = conn.cursor()
            cursor.execute('create table if not exists %s (time float primary key, name char(20),used int DEFAULT 0,total int)' % tableName)
            cursor.execute('insert into %s (time,name,used,total) values (\'%f\',\'%s\',\'%d\',\'%d\')' %(tableName,curTime,roomName,used,total))
            cursor.close()
            conn.commit()
            conn.close()
    except requests.exceptions.RequestException:
        print requests.exceptions


def main():
    parse()

if __name__ == '__main__':
    main()
