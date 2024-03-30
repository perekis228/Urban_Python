def CaesarEncode(string):
    coded_string = ''
    for i in range(len(string)):
        if string[i] == 'э' or string[i] == 'ю' or string[i] == 'я' or\
           string[i] == 'Э' or string[i] == 'Ю' or string[i] == 'Я':
            coded_string += chr(ord(string[i]) - 29)
        else:
            coded_string += chr(ord(string[i])+3)
    return coded_string

def CaesarDecode(string):
    decoded_string = ''
    for i in range(len(string)):
        if string[i] == 'а' or string[i] == 'б' or string[i] == 'в' or \
                string[i] == 'А' or string[i] == 'Б' or string[i] == 'В':
            decoded_string += chr(ord(string[i]) + 29)
        else:
            decoded_string += chr(ord(string[i]) - 3)
    return decoded_string

sentence = "Цезарь родился в 100 году до н.э."
encoded_sentence = CaesarEncode(sentence)
print(encoded_sentence)
decoded_sentence = CaesarDecode(encoded_sentence)
print(decoded_sentence)