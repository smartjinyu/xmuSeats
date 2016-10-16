### Xiamen University Seats Usage Analysis Project

A project in order to collect seats usage situation in Xiamen University Library and then do some data analysis on them. Here is the Web Crawler code and the data collected by me. More information about this project can be found [on my blog].

[on my blog]:http://smartjinyu.com/data/mining/2016/10/12/XMU_Lib_Seats.html


#### About the Crawler

The web crawler is written in Python 2.7.11 and has tested on Windows 10, Ubuntu 16.04 and CentOS 7. It uses Sqlite3 to store the data collected. The program is fully Open Source under GPL V3 Lincense.

#### Dependencies
 - Requests 2.7.0
 - Beautiful Soup 4.3.2
 - lxml 
 - sqlite3
 - time

#### About the DataBase

After runnings the program, it will create a sqlite3 database named 'seatState.db' in current directory. This database have 14 tables named 'roomstate1' to 'roomstate14'. Each table represents the usage data of a reading room in Xiamen University Library. And each table has four attributes, which are time(float),RoomName(char),used(int),total(int).


#### About the Data

I run this web crawler on my Virtual Private Server and collect data every 2 minutes. I will share the data every Sunday. You can use it for data analysis purpose if you specify the source information. 


If you have any advise or complaints, please feel free to contact me.