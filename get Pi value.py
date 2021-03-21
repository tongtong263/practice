#pi.py
from random import random
from math import sqrt
import time

DARTS = 1200
hits = 0
time.process_time()

for i in range(1, DARTS):
    x, y = random(), random()
    dist = sqrt(x**2 + y**2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/DARTS)
print("Pi的值是 %s" % pi)
print("程序运行时间是 %-5.5ss" % time.process_time())