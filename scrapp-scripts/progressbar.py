import time
import sys

bar = "#"

# for i in range(1,10):
#     bar = ("#" * i)
#     sys.stdout.write('\r'+bar)
#     time.sleep(1)

for i in range(0, 101):
    sys.stdout.write('\r[' + ('.' * i) + (' ' * (100 - i) + ']') + '(' + str(i) + '%)')
    time.sleep(.1)

