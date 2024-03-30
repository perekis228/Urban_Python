def SumRange(min, max):
    sum = 0
    for i in range(min, max+1):
        sum += i
    return sum
print(SumRange(1,10))