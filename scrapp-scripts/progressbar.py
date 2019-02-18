import time
import sys

bar = "#"

for i in range(1,10):
    bar = ("#" * i)
    sys.stdout.write('\r'+bar)
    time.sleep(1)
