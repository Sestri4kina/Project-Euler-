#the sum of the primes bellow two million
import math

def pr_sum():
    prime = [2]
    sum = 2
    while prime[len(prime)-1] <2000000:
        for i in range(3,2000000,2):
            if all(i%n != 0 for n in range(2, int(math.sqrt(i))+1 )):
                prime.append(i)
                sum += i
        return sum

print pr_sum()
	

        
