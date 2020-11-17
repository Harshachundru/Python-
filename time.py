Python 3.8.1 (tags/v3.8.1:1b293b6, Dec 18 2019, 23:11:46) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import time as t
>>> t.localtime()
time.struct_time(tm_year=2020, tm_mon=2, tm_mday=21, tm_hour=15, tm_min=47, tm_sec=16, tm_wday=4, tm_yday=52, tm_isdst=0)
>>> time_now = t.localtime()
>>> print("The transaction time is ", str(time_now.tm_hour)+'h'+str(time_now.tm_min)+'m')
The transaction time is  15h47m
>>> t.time()
1582280395.0797603
>>> t.time()
1582280401.7534342
>>> time_now = t.time()
>>> delivery time = time_now + (86400*7)
SyntaxError: invalid syntax
>>> delivery_time = time_now + (86400*10)
>>> print("The delivery time is :", t.localtime(delivery_time))
The delivery time is : time.struct_time(tm_year=2020, tm_mon=3, tm_mday=2, tm_hour=15, tm_min=50, tm_sec=20, tm_wday=0, tm_yday=62, tm_isdst=0)
>>> t.sleep(10)
>>> 