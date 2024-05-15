with open('text.txt', 'r') as file:
    print(file.read())
'''
with открывает файл и после блока кода, содержащегося в нём, закрывает файл.
Если открыть без with, то, пока мы сами не напишем close(), файл будет открыт.
То есть, если мы забудем закрыть файл, то он будет занимать память просто так.
'''