import sys
import time


for i in range(100):
    k = i + 1
    str1 = '>' * i + ' ' * (100 - k)
    #sys.stdout.write('\r' + str1 + '[%s%%]' % (i + 1))
    #sys.stdout.flush()
    print('\r' + str1 + '[%s%%]' % (i + 1),end = '')
    time.sleep(0.1)
