import random
import math
from collections import Counter

digitstring = '0123456789'
otprandomlist = []
otprandomrangelist = []

def otprandom(ds):
    otp = ""
    for _ in range(6):
        pos = random.random()
        otp += ds[math.floor(pos*10)]
    return otp


def otprandomrange(ds):
    otp = ""
    digitstring = '0123456789'
    for _ in range(6):
        pos = random.randrange(0, 10, 1)
        otp += ds[pos]
    return otp



for _ in range(10000):
    otprandomlist.append(otprandom(digitstring))
    otprandomrangelist.append(otprandomrange(digitstring))
    # print(_+1)
    # print('Random: '+otprandom(digitstring))
    # print('RandomRange: ' + otprandomrange(digitstring))


Crandom = Counter(otprandomlist)
CrandomRange = Counter(otprandomrangelist)


RandomRepeats = 0
for _ in Crandom.most_common():
    if _[1] > 1:
        RandomRepeats += _[1]-1
print('Random Repeats: '+str(RandomRepeats))

RRRepeats = 0
for _ in CrandomRange.most_common():
    if _[1] > 1:
        RRRepeats += _[1]-1
print('Random range repeats:' +str(RRRepeats))




