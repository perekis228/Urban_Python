
def is_prime(func):
    def wrapper(a, b, c):
        num = func(a, b, c)
        prime = True
        for i in range(2, num // 2 + 1):
            if (num % i == 0):
                print('Составное')
                prime = False
                break

        if prime:
            print('Простое')

        return num
    return wrapper

@is_prime
def sum_three(a, b, c):
    return a + b + c

result = sum_three(2, 3, 6)
print(result)