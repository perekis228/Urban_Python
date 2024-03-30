import random
def Sort(list_):
    for i in range(len(list_)-1):
        for j in range(i+1, len(list_)):
            if list_[i] < list_[j]:
                temp = list_[j]
                list_[j] = list_[i]
                list_[i] = temp
    return list_
list_ = []
for i in range(10):
    list_.append(random.randint(0, 50))
print("До сортировки:", list_)
print("После сортировки:", Sort(list_))
print("Максимальное:", list_[0])