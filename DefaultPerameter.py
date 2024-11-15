def  sumValue(a,b,c=10):"""parameter overwrite. Default parameter must be included from right to left"""
    sum = a+b+c
    return sum
print(sumValue(10,20,))