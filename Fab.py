def fab(n):
    n1 = 1
    n2 = 1
    n3 = 1
    if n < 1:
        print('输入有误!')
        return -1
    while (n-2) > 0:
        n3 = n2 + n1
        n1 = n2
        n2 = n3
        n -= 1
    return n3
result = fab(20)
if result != -1:
    print('总共有%d对兔子'% result)

def fab2(n):
    if n < 1:
        print('输入有误!')
        return -1
    if n == 1 or n == 2:
        return 1
    else:
        return fab2(n-1) + fab(n-2)
result = fab2(20)
if result != -1:
    print('总共有%d对兔子' % result)
