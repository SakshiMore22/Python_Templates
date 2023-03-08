mod= 1000000007
def fact(n):
    ans=1
    for i in range(2,n+1):
        ans=(ans*i)%mod
    return ans
def modInverse(b,m):
    return pow(b, m - 2, m)
 
def modDivide(a,b,m):
    a = a % m
    inv = modInverse(b,m)
    return (inv*a) % m
def comb(n,k):
    return modDivide(fact(n),(fact(k)*fact(n-k)),mod)
