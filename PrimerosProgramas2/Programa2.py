'''
Created on 28 sept. 2017

@author: juamar
'''
def gcd(x, y):
    if (x < 1 or y < 1):
        return "Los dos numero deben de ser enteros positivos."
    else:
        if (x < y):
            lesser = x
        else:
            lesser = y
            
        for i in range(1, lesser + 1):
            if x % i == 0 and y % i == 0:
                max_divisor = i
        
        return max_divisor
        

print(gcd(1, 12))
print(gcd(6, 12))
print(gcd(9, 12))
print(gcd(17, 12))
