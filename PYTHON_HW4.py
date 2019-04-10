#Euclid Algorithm for GCD [defined recursively, because its easier...?]
def gcd(a, b): 
    if a < b:
        return gcd(a, b-a)
    elif b < a:
        return gcd(a-b,a)
    else: 
        return a

#Test Case
print (gcd(128, 60))
input("Press Enter to continue...")