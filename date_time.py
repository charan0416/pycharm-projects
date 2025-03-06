from datetime import date
from datetime import time
from datetime import datetime


print(date.today())
print(date.today().weekday())
print(time.min)
print(time.max)
today = date.today()
print(today)
print(today.strftime("%Y:%m:%d"))
print()

date_now = datetime.datetime.now()
date_now_ts = date_now.timestamp()
back_date_ts = back_date.timestamp()
print(date_now_ts)