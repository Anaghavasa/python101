#dates are very compicated
from datetime import datetime
current_date=datetime.now()
print("Today is "+str(current_date))
print("Day:"+str(current_date.day))
print("Month:"+str(current_date.month))
print("Year:"+str(current_date.year))
#how to write birthdays
birthday=input("enter your birthday:dd/mm/yyyy ")
birthday_date=datetime.strptime(birthday, "%d/%m/%Y")
print("birthday:"+str(birthday_date))

               
