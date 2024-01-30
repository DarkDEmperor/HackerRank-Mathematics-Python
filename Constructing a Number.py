'''
Manipulating numbers is at the core of a programmer's job. To test how well you know their properties, you are asked to solve the following problem.
You are given  non-negative integers a1, a2, ..., an. You want to know whether it's possible to construct a new integer using all the digits of these numbers such that it would be divisible by 3. 
You can reorder the digits as you want. The resulting number can contain leading zeros. Thanklhg
'''

def canConstruct(a):
    # Return "Yes" or "No" denoting whether you can construct the required number.

    res, s = (''.join([str(i) for i in a])), 0
    for i in res: s += int(i)
    if s % 3 == 0: return 'Yes'
    return 'No'
