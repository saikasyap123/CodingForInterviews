def Arr_Man(arr, n):
    p=0
    while p < len(arr):
        q = p +1
        
        while q < len(arr):
            r = q + 1
            
            while r < len(arr):
                
                if arr[p] + arr[q] + arr[r] == n :
                    print(list([arr[p],arr[q],arr[r]]))
                r +=1
            q +=1
        p +=1
        
    
print("Enter the elements with space in between")
tokens = input().split()
Num_Array = [int(x) for x in tokens]
n = int(input("Enter the required sum:"))
Arr_Man(Num_Array, n)