#10. Write a python script to display the current date and time. First create variables to
#store date and time, then display date and time in proper format (like: 13-8-2022 and
#9:00 PM)
from datetime import datetime

dt = datetime.today()
print(dt)

d1 = dt.strftime("%H: %M: %S") # This is 24 hours time formate
print(d1)

d1 = dt.strftime("%d- %m -%Y") 
print(d1)

