#!usr/bin/python
# This script will do some data preprocess(abort invalid data, adjust time,e.t.c.)
# and export them into a Microsoft Excel document
# Caution that this script is only compatible with the old schema of database (from OCT 14,2016 to DEC 15,2016, named seatState_old.db in my GitHub Repository)
# This script is NOT compatible with the new schema of database, named libseat.db
__author__ = 'smartjinyu'
import sqlite3
import xlwt
import time

def main():
    workbook = xlwt.Workbook(encoding='ascii')
    conn = sqlite3.connect('seatState.db')
    cursor = conn.cursor()
    i = 1
    totalrow = 0
    while(i<=14):
        print 'Processing Roomstate' + str(i)
        worksheet = workbook.add_sheet('Roomstate'+str(i))
        cursor.execute('select * from Roomstate'+str(i))
        worksheet.write(0,0,'Year')
        worksheet.write(0,1,'Month')
        worksheet.write(0,2,'Day')
        worksheet.write(0,3,'Hour')
        worksheet.write(0,4,'Minute')
        worksheet.write(0,5,'Weekday')
        worksheet.write(0,6,'Used')
        worksheet.write(0,7,'Total')
        xlsrow = 1
        for row in cursor:
            timeturple = time.gmtime(row[0])
            year = timeturple[0]
            month =  timeturple[1]
            day =  timeturple[2]
            hour = timeturple[3]+8
            minute = timeturple[4]
            weekday = timeturple[6]
            if(weekday == 3 and hour >= 13 and  hour <=17):
                continue #the library will close on Wednesday afternoon 13 pm - 18 pm
            if(hour == 21 and minute >= 30):
                continue #abort data after 21.30 pm
            if(hour >= 22):
                continue
            if(year == 2016 and month == 12 and day >= 10 and day <=11):
                hour = hour - 8 #due to incorrect time setting in VPS
            if(year == 2016 and month == 10 and day ==12 or day == 13):
                continue #abort the first two days


            used = row[2]
            total = row [3]
            worksheet.write(xlsrow, 0, year)
            worksheet.write(xlsrow, 1, month)
            worksheet.write(xlsrow, 2, day)
            worksheet.write(xlsrow, 3, hour)
            worksheet.write(xlsrow, 4, minute)
            worksheet.write(xlsrow, 5, weekday)
            worksheet.write(xlsrow, 6, used)
            worksheet.write(xlsrow, 7, total)
            xlsrow = xlsrow + 1
        print 'Roomstate' + str(i) + ' finished'
        i=i+1
        totalrow = totalrow + xlsrow
    conn.close()
    print 'Total Entries is ' + str(totalrow)
    workbook.save('seatState.xls')


if __name__ == '__main__':
    main()