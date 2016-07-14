# looking for the 10001st prime number
import math

def pr():
    prime = [2]
    while len(prime)<10001:
        for i in range(3,1000000,2):
            if all(i%n != 0 for n in range(2, int(math.sqrt(i))+1 )):
                prime.append(i)
        return prime[10000]

print pr()
