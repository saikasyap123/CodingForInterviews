def f1(a1, a2, a3):
    Num_Arr = []
    for i in a1:
        if i in a2 and i in a3:
            Num_Arr.append(i)
    Num_Arr.sort()
    return Num_Arr

print('Elements of 1st Array:')
tokens_1 = input().split()
Arr1 = [int(x) for x in tokens_1]
print('Elements of 2nd Array:')
tokens_2 = input().split()
Arr2 = [int(x) for x in tokens_2]
print('Elements of 3rd Array:')
tokens_3 = input().split()
Arr3 = [int(x) for x in tokens_3]
print(f1(Arr1, Arr2, Arr3))