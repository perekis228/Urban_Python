def test(*args):
    for i in args:
        print(i)
test(1, 2.2, True, 'str')

def factorial(num):
    if num > 1:
        return num*factorial(num-1)
    return 1
print('Факториал:', factorial(5))