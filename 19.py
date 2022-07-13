# https://www.programiz.com/python-programming/datetime
from datetime import date, timedelta

def allsundays(year):
   d = date(year, 1, 1)                    # January 1st
   d += timedelta(days = 6 - d.weekday())  # First Sunday
   while d.year == year:
      yield d
      d += timedelta(days = 7)

count = 0   
for i in range (1901,2001):
   for d in allsundays(i):
      if d.day == 1:
         count += 1

print (count)