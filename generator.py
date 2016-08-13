'''import random

def lottery():
    for i in xrange(6):
        yield random.randint(1,40)


    yield random.randint(1,15)


for i in lottery():
    print "And the next number is %d" % i

'''
a=1
b=1
def fib():
    
    a,b = 1, 1   
    while 1:
        yield a
        a, b = b, a + b

count =0
for i in fib():
    print i
    count+=1
    if count == 10:
        break; 



