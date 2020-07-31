def Arr_Man1(arr):
    Num_Arr = []
    for i in arr:
        if i != 0:
            Num_Arr.append(i)
    if len(Num_Arr)<len(arr):
        while (len(Num_Arr)<len(arr)):
            Num_Arr.append(0)
    return Num_Arr
        
        
tokens = input().split()
arr = [int(x) for x in tokens]
print(Arr_Man1(arr))