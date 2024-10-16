from dateutil.rrule import weekday

weekday = {1:"Monday", 2:"Tuesday", 3:"Wednesday", 4:"Thursday", 5:"Friday", 6:"Saturday", 7:"Sunday"}
weekday_1 = []
for i in weekday:
    weekday_1 += (weekday[i], i)
print(weekday)
print(weekday_1)