import os
import datetime
import time


ping = os.system("ping -c  3 8.8.8.8")
now = datetime.datetime.now().strftime('%d %b %H:%M')
if ping == 0:
	print("last status is OK {0}\n".format(now))
else:
	print("last status is FAILD {0}\n".format(now))
