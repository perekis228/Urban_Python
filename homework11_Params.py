# Функция с параметрами по умолчанию
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params(10)
print_params(11, 'False')
print_params(2, 'abc', False)
print_params(b = 25)                  # Работает
print_params(c = [1,2,3])             # Работает


# Распаковка параметров
values_list = [5, 'smth', False]
values_dict = {'a': 11, 'b': 'kuku', 'c': False}
print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [1, 2.3]
print_params(*values_list_2, 42)   # Работает