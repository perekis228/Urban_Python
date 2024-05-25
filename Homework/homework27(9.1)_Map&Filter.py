def square(x):
    return x ** 2

def odd(x):
    return x % 2

nums = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]
res = list(filter(odd, map(square, nums)))
print(res)