#Firstly the great euclids algorithm to find gcd between two numbes:
def gcd(a,b):
    if b == 0 :
        return a
    else :
        return gcd(b,a%b)
#In extended euclids algorithm, this function also returns two constants c1 and c2 such that gcd(a,b) = c1a+c2b 

def extended_euclid_gcd(a,b): #returns (c1,c2,g). g denotes gcd
    if b==0 : 
        return (1 , 0 , a)
    else :
        (c1,c2,g) = extended_euclid_gcd(b,a%b)
        return (c2 , c1 - a//b *y , g)
     
#working:
#if b=0 then 1*a + 0*b = a fits eqn
# else:
# gcd(a,b)=c1a+c2b=gcd(b,a%b)=c1(b)+c2(a%b) ........(i)
# also a = (a//b)*b + a%b ...........(ii)
# so c1b + c2(a-a*b//b) = g
# ie. a*c2 + b*(c1-a//b *c2) = g .....(iii)
# from i and iii:
# a*c1 + b*c2 = a*c2 + b *(c1-a//b *c2) = g
# hence (c1,c2,gcd(a,b)) = (c2 , c1-a//b*c2 , gcd(b,a%b))
