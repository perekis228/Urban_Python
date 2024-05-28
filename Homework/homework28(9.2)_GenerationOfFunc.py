#1
def makeFunc(op):
    if op == '+':
        def sum(x, y):
            return x + y
        return Sum

    elif op == '-':
        def sub(x, y):
            return x - y
        return Sub

    elif op == '/':
        def div(x, y):
            try:
                return x / y
            except ZeroDivisionError:
                return 'Не делите на ноль!'
        return Div

    elif op == '*':
        def mult(x, y):
            return x * y
        return Mult

    else:
        raise Exception(f'Неизвестный оператор "{op}"')

funcSum = makeFunc('+')
print(funcSum(5, 6))
funcDiv = makeFunc('/')
print(funcDiv(4, 0))

#2
func = lambda x, y: x ** y
print(func(2, 3))

def deg(x, y):
    return x ** y
print(deg(2, 3))

#3
class Rect:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __call__(self):
        return self.a * self.b

obj = Rect(3, 4)
print(obj())
