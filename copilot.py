### Make my computer shut down after 30 seconds
### Count down before shutting down

import time
import os

countdown = 30

while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)

os.system("shutdown /s")

