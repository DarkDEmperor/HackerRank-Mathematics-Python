'''
A Smith number is a composite number, the sum of whose digits is the sum of the digits of its prime factors 
obtained as a result of prime factorization (excluding 1). The first few such numbers are 4, 22, 27, 58, 85, 94, and 121.
'''

def primefactorsum(n):
    factors, factorsum = '', 0
    while n > 1:
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                factors += str(i)
                n //= i
                break
        else:
            factors += str(n)
            break
            
    for i in factors: factorsum += int(i)
    return factorsum
 
def digitsum(n, dsum = 0):
    for i in str(n): dsum += int(i)
    return dsum

def solve(n):
    if primefactorsum(n) == digitsum(n): return 1
    return 0
