def SignCount(string):
    signs = {}
    sign = ''
    count = 0
    for i in string:
        signs[i] = signs.get(i, 0) + 1
    for key, value in signs.items():
        if value > count:
            sign = key
            count = value
    print(f'Самая часто встречающаяся буква: "{sign}", она встречается {count} раз')


string = "Таким образом, высокое качество позиционных исследований говорит о возможностях распределения внутренних резервов и ресурсов."
SignCount(string)