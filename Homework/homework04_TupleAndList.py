#2
immutable_var = (1, 2.2, False, "str")
print("Immutable tuple:", immutable_var)

#3
#immutable_var[0] = 2 # Нельзя присвоить новое значение, так как кортеж неименяем

#4
mutable_list = [1, 2.2, False, "str"]
mutable_list[0] = 2
mutable_list[1] = 3.3
mutable_list[2] = True
mutable_list[3] = "new"
print("Mutable list:", mutable_list)
