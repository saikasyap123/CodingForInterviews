def f3(arr):
    Num_set = {}
    odd_set = []
    even_set = []
    for i in arr:
        Num_set[i]=arr.count(i)
    for i in Num_set:
        if Num_set[i]%2==0:
            even_set.append(i)
        elif Num_set[i]%2==1:
            odd_set.append(i)
    if len(odd_set) ==1:
        return odd_set[0]
    elif len(even_set)==1:
        return even_set[0]
    
    
tokens = input().split()
arr = [int(x) for x in tokens]
print(f3(arr))