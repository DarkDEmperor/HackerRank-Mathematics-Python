'''
You are given 3 numbers a, b and x. You need to output the multiple of x which is closest to ab.
If more than one answer exists , display the smallest one.
'''

def closestNumber(a, b, x):
    rem = a**b % x
    if rem <= x // 2:
        return int(a ** b - rem)
    else:
        return int(a ** b - rem + x)
