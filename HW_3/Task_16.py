import random
N = int(input('Enter the number of elements in the array: '))
lst = [random.randint(0, 10) for i in range(N)]
print(lst)
x = int(input('Enter the element you are looking for: '))
print(x)
lst_1 = []
ind = 0
for i in lst:
    if x == lst[ind]:
        lst_1.append(x)
        ind += 1
    else: ind += 1

print(lst_1)
print(len(lst_1))