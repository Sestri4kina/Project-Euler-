#special Pythagorean Triplet a+b+c=1000, looking for the product a*b*c

def PT():
    for c in range(1,700):
        for b in range(1,500):
            for a in range(1,300):
                if a**2 + b**2 == c**2 and a+b+c == 1000:
                    return a*b*c

print PT()
