#looking for the smallest positive number that is evenly divided by numbers from 1 to 20
def list_of_primers(n):
    primers = [2]
    for i in range(3,n,2):
        primers = [ i for j in range(2,n) if i%j!=0]
    return primers
                
        
print list_of_primers(20)

def smallest_number():
    primers = [2, 3, 5, 7, 11, 13, 17, 19]
    n=1
    for i in primers:
        for j in range(1,10):
            if (i**(j-1) < 20) & (i**j > 20):
                k = i**(j-1)
                n = n*k
    return n

print smallest_number()
           
        

