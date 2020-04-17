#video from python
first_number=123
second_number=123
print(first_number+second_number)
print(second_number*first_number)
#if you add a number and a string it will
#blow up because it is confused if it is a number or string
#dates time function and libary
from datetime import datetime
current_date=datetime.now()
print("Today is "+str(current_date))
print("Day:"+str(current_date.day))
print("Month:"+str(current_date.month))
print("Year:"+str(current_date.year))
