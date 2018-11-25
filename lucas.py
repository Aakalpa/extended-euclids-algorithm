# lucas theorem to calc C(n,r) % m if m is prime
memory = {} #creating a dictionary to store C(n,r,m) where 0<=r<=n<=9 .
# creating dictionary here also demonstrates memoization
def C(n,r,m):
    if r < 0 or r > n : return 0
    if r == 0 or r == n : return 1
    if n > m :
        return C(n%m,r%m,m) * C(n//m,r//m,m) % m
    if (n,r,m) not in memory:
        memory[(n,r,m)] = (C(n-1,r,m) + C(n-1,r-1,m)) % m #calculating C() recursively
    print(memory)
    return memory[(n,r,m)]
print(C(234,98,7)) #prints 6

