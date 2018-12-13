from itertools import cycle
import time


lights = ['red', 'green', 'amber']
for each in cycle(lights):
    print(each)
    time.sleep(1)
