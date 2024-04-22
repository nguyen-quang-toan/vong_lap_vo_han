import datetime
import time
import random

color = ['\033[30m', '\033[31m',
         '\033[32m', '\033[33m',
         '\033[34m', '\033[35m',
         '\033[36m', '\033[37m',
         '\033[38m', '\033[39m',]

anniversary = datetime.date(2024, 2, 20)

while True:
    i = random.randint(0, 9)
    print(color[i] +
          anniversary.strftime("%d-%m-%Y"),
          ": Yêu Ngọc Hà Nhứt Trên Đời ", sep="")

    time.sleep(0.01)
    anniversary += datetime.timedelta (days = 1)