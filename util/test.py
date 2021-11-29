import os
import random
import time
print(os.path.join(os.path.abspath(os.path.dirname(os.path.dirname(__file__)))+'/config/'+'LocalElement.ini'))
for i in range(5):
    result = []
    result1 = []
    for i in range(6):
        num = random.randint(1,33)
        if num not in result:
            result.append(num)
        else:
            num = random.randint(1, 33)
            if num not in result:
                result.append(num)


    #print(result)
    for i in range(1):
        num = random.randint(1,12)
        if num not in result1:
            result1.append(num)
        else:
            num = random.randint(1, 16)
            if num not in result1:
                result1.append(num)

    result.sort()
    result1.sort()
    print('前区是：',result,'后区是：',result1)
nowtime = time.strftime("%Y-%m-%d %H:%M:%S")
a = '11'
print('%s%s'%(a,nowtime))

