def method1():
    sum=0
    for i in range (1001, 1000000):
        left_part = i // 1000
        right_part = i % 1000
        if (left_part//100 + (left_part % 100)//10 + (left_part % 100) % 10) == (right_part//100 + \
            (right_part % 100)//10 + (right_part % 100) % 10):
            sum += 1
    print 'Method 1'
    print 'Amount of happy tickets: %d' % sum


def method2():
    sum= 0
    for a in range(10):
        for b in range(10):
            for c in range(10):
                for d in range(10):
                    for e in range(10):
                        for f in range(10):
                            if a+b+c == d+e+f:
                                sum += 1
    sum = sum - 1
    #Except ticket No 000000
    print 'Method 2'
    print 'Amount of happy tickets: %d' % sum

method1()
method2()

