"""def factorialCount(n):
    print(n)
    fact = 1
    for i in range(1,n+1):
        fact=fact*i
        i +=1
    return fact

print(factorialCount(int(input("Enter The Number: "))))"""


def factorialCount(n):
    print(n)
    fact = 1
    i = 1
    while (i < n + 1):
        fact = fact * i
        i += 1
    return fact


print(factorialCount(int(input("Enter The Number: "))))
