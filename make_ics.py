# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 13:12:57 2018

@author: Helen YU Yu
"""

import xlrd

data = xlrd.open_workbook("C:\\Users\\Helen YU Yu\\iCloudDrive\\Desktop\\\Make_Plan.xlsm")
table = data.sheet_by_name(u'ics')
nrows = table.nrows
eventString = ""
icsString = "BEGIN:VCALENDAR\nMETHOD:PUBLISH\nVERSION:2.0\nX-WR-CALNAME:课程表\nPRODID:-//Apple Inc.//Mac OS X 10.12//EN\nX-APPLE-CALENDAR-COLOR:#FC4208\nX-WR-TIMEZONE:Asia/Shanghai\nCALSCALE:GREGORIAN\nBEGIN:VTIMEZONE\nTZID:Asia/Shanghai\nBEGIN:STANDARD\nTZOFFSETFROM:+0900\nRRULE:FREQ=YEARLY;UNTIL=19910914T150000Z;BYMONTH=9;BYDAY=3SU\nDTSTART:19890917T000000\nTZNAME:GMT+8\nTZOFFSETTO:+0800\nEND:STANDARD\nBEGIN:DAYLIGHT\nTZOFFSETFROM:+0800\nDTSTART:19910414T000000\nTZNAME:GMT+8\nTZOFFSETTO:+0900\nRDATE:19910414T000000\nEND:DAYLIGHT\nEND:VTIMEZONE\n"
for i in range(nrows):
    eventString = eventString+"BEGIN:VEVENT\nCREATED:"+table.row_values(i+1)[0]
    eventString = eventString+"\nUID:"+table.row_values(i+1)[1]
    eventString = eventString+"\nDTEND;TZID=Asia/Shanghai:"+table.row_values(i+1)[2]
    eventString = eventString+"00\nTRANSP:OPAQUE\nX-APPLE-TRAVEL-ADVISORY-BEHAVIOR:AUTOMATIC\nSUMMARY:"+table.row_values(i+1)[5]
    eventString = eventString+"\nDTSTART;TZID=Asia/Shanghai:"+table.row_values(i+1)[6]
    eventString = eventString+"\nDTSTAMP:"+table.row_values(i+1)[7]
    eventString = eventString+"\nSEQUENCE:0\nBEGIN:VALARM\nX-WR-ALARMUID:"+table.row_values(i+1)[9]
    eventString = eventString+"\nUID:"+table.row_values(i+1)[10]
    eventString = eventString+"\nTRIGGER:"+table.row_values(i+1)[11]
    eventString = eventString+"\nDESCRIPTION:事件提醒\nACTION:DISPLAY\nEND:VALARM\nEND:VEVENT\n"
icsString = icsString + eventString + "END:VCALENDAR"