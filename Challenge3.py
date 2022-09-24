import math
numPrimes=input("How many primes do you want? - ")
while numPrimes.isnumeric==False:
    numPrimes=input("How many primes do you want? - ")
numPrimesFound=0
numberChecking=2

def isPrime(n):
    if n==2:
        return True
    if n % 2 == 0 or n<=1:
        return False
    for I in range(3,n):
        if n % I==0:
            return False

    return True


while numPrimesFound<int(numPrimes):
    if isPrime(numberChecking) ==True:
        print(str(numberChecking))
        numPrimesFound+=1
    if numberChecking==2:
        numberChecking+=1
    else:
        numberChecking+=2
