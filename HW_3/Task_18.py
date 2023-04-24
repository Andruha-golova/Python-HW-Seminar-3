import random
N = int(input('Enter the number of elements in the array: '))
lst = [random.randint(1, 5) for i in range(N)] 
print(lst)
x = int(input('Enter a natural number to compare: '))
print(x)
ind = 0
min = abs(x - lst[0])
for i in range(1, N):
    dif = abs(x - lst[i])
    if dif < min:
        min = dif
        ind = i
print(lst[ind])