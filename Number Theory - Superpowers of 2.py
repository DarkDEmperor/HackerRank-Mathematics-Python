'''
You will be given two integers a, b. You are required to output the result of 2^(2^a) mod b.
'''

def solve(a, b):
    # Write your code here
    return pow(2, 2 ** a, b)
