#2
my_string = input("Enter the string: ")
print("Length:", my_string.__len__())

#3
print("UpperCase: ", my_string.upper())
print("LowerCase: ", my_string.lower())
print("Without spaces: ", my_string.replace(" ", ""))
print("First letter: ", my_string[0])
print("Last letter: ", my_string[my_string.__len__()-1])