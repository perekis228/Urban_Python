def Braces(string):
    count1 = 0
    count2 = 0
    count3 = 0
    count4 = 0
    closeCount = 0
    exist = True
    for i in string:
        if i == '<': count1 += 1
        elif i == '{': count2 += 1
        elif i == '(': count3 += 1
        elif i == '[':count4 += 1
        elif i == '>':
            count1 -= 1
            closeCount += 1
        elif i == '}':
            count2 -= 1
            closeCount += 1
        elif i == ')':
            count3 -= 1
            closeCount += 1
        elif i == ']':
            count4 -= 1
            closeCount += 1
        if count1 < 0 or count2 < 0 or count3 < 0 or count4 < 0:
            exist = False
            break
    if count1 != 0 or count2 != 0 or count3 != 0 or count4 != 0:
        exist = False

    if exist:
        for i in range(closeCount):
            if '<>' in string:
                string = string.replace('<>', '')
            elif '{}' in string:
                string = string.replace('{}', '')
            elif '()' in string:
                string = string.replace('()', '')
            elif '[]' in string:
                string = string.replace('[]', '')
            elif string != '':
                exist = False
                break
    return 'YES' if exist else 'NO'
smth = '<{[](())[(]){}}>'
print(Braces(smth))
