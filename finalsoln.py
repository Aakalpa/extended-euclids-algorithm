memo={}
def C(n,r,p):
    #calculates C(n,r) % p where p is a prime number using lucas theorem
    if r==0 or r==n:
        return 1
    if r<0 or r>n :
        return 0
    if n>p :
        return C(n%p,r%p,p) * C(n//p,r//p,p) % p
    if (n,r,p) not in memo:
        memo[(n,r,p)] = ( C(n-1,r,p) + C(n-1,r-1,p) ) % p
    return memo[(n,r,p)]
def extended_euclid_gcd(a,b):
    #returns (c1,c2,g) such c1*a + c2*b = g
    if b==0:
        return (1,0,a)
    (c1,c2,g) = extended_euclid_gcd(b,a%b)
    return (c2 , c1 - (a//b)*c2 , g)
p=[]
n,r,m = 5,2,1001
for i in [2,3,5,7,9,11,13,17,19,23,29,31,37,41,43,47]:
    if m%i == 0 :
        p.append((i,C(n,r,i)))
        m/=i
    if m == 1 :
        break
print(p)
ans = p[0]
for x in p[1:]:
    (c1,c2,g) = extended_euclid_gcd(x[0]*ans[1] , x[1]*ans[0])
    ans = (ans[0]*x[0] , (c1*ans[1]*x[0] + c2*ans[0]*x[1]) % (ans[0]*x[0]))
print(ans[1])




