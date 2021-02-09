# 1408 : 24

# code for submitting
from datetime import timedelta

now_h, now_m, now_s = map(int, input().split(":"))
start_h, start_m, start_s = map(int, input().split(":"))

now = timedelta(hours=now_h, minutes=now_m, seconds=now_s)
start = timedelta(hours=start_h, minutes=start_m, seconds=start_s)

if (now < start):
    finish = str(start-now)
else:
    finish = str(timedelta(hours=24) - (now - start))
    
if (len(finish) == 7):
    finish = '0' + finish

print(finish)