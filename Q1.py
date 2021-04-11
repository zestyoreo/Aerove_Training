import math as m

def is_prime(n):
    prime_bool=True
    if n==1:
        return False
    for i in range(2,m.ceil(m.sqrt(n))+1):
        if n%i==0:
            prime_bool=False
            break
    return prime_bool

a=int(input("Enter number of decimal places: "))-1
primes=[]
for i in range(10**a,10**(a+1)-1):
    if is_prime(i):
        primes.append(i)

file1=open("myFirstFile.txt","w")

for j in range(1,len(primes)):
    if primes[j-1]+2==primes[j]:
        file1.write(str(primes[j-1])+" "+str(primes[j])+"\n")

file1.close()