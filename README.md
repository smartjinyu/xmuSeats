
### Xiamen University Seats Usage Analysis Project

A project in order to collect seats usage situation in Xiamen University Library and then do some data analysis on them. Here is the Web Crawler code and the data collected by me. More information about this project can be found [on my blog].

[on my blog]:https://smartjinyu.com/datamining/2016/10/12/XMU_Lib_Seats.html

#### Caution

This project has moved to new schema of database since DEC 16,2016. The new database is named libseat.db. The data collected from OCT 14,2016 to DEC 15,2016 are stored in seatState_old.db.

#### About the Crawler

The web crawler is written in Python 2.7.11 and has tested on Windows 10, Ubuntu 16.04 and CentOS 7. It uses sqlite3 to store the data collected. Caution that you may meet gibberish problem when you open the database under Windows. The program is fully Open Source under GPL V3 Lincense.

#### Dependencies
 - Requests 2.7.0
 - Beautiful Soup 4.3.2
 - lxml 
 - sqlite3
 - time

#### About the DataBase

**New Database**: The new database is named libseat.db, covering data from DEC 16,2016 till now. The new schema is much more simple and can save a lot of space, so that I will collect data every minute. It will updated every week.

![newdb](https://smartjinyu.com/img/2016-10-12/libseat.png)


**Old Database**: The old database is named seatState_old.db, it covers data from CT 14,2016 to DEC 15,2016 (collect every 2 minutes). This database will NOT update anymore.

![newdb](https://smartjinyu.com/img/2016-10-12/seatState.png)

#### Problems in the Data

According to the following reasons, data may be inaccurate and you may need to do some data cleaning work before data analysis. For seatState_old.db, preprocess.py can finish such work automatically.
1. The library will close every Wednesday afternoon from 1 p.m. to 6 p.m., when students are not allowed to enter the library.
2. The seat usage data becomes zero after 21:30 every day, not 22:00.
3. You need to add 8 hours when using data from DEC 9,2016 to DEC 11,2016, and these data may be incomplete. (Sorry for my wrong VPS timezone settings)


#### About the Data

I run this web crawler on my Virtual Private Server and collect data every minute (every 2 minutes in seatState_old.db). I will share the data every Sunday. You can use it for data analysis purpose if you specify the source information. 


If you have any advise or complaints, please feel free to contact me.