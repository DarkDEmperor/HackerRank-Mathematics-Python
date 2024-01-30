'''
You are given an integer N. Is there a permutation of digits of integer that's divisible by 8? 
A permutation of digits of integer N is defined as an integer formed by rearranging the digits of N. 
For example, if the number N = 123, then {123, 132, 213, 231, 312, 321} are the possible permutations.
'''

def solve(n):
    # Write your code here
    n = str(n)
    
    if n == '8' or n == '0': return 'YES'
    if len(n) == 2:
        if int(n) % 8 == 0 or int(n[:: -1]) % 8 == 0: return 'YES'
        else: return 'NO'
        
    for i in p(n, 3):
        if int(''.join(i)) % 8 == 0:
            return 'YES'
            
    return 'NO'
