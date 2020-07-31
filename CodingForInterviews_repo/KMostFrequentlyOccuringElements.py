n = int(input())
tokens = input().split()
NumArray = [int(x) for x in tokens]
NumHash = {}
for i in NumArray:
    NumHash[i] = NumArray.count(i)
print("Required elements are...")
for i in NumHash:
    if NumHash[i] == n:
        print(i)
        
        
tokens = input().split()
NumArray = [int(x) for x in tokens]
n = int(input())
fun3(NumArray, n)

def fun3(arr, n):
    NumHash = {}
    for i in arr:
        NumHash[i] = arr.count(i)
    for i in NumHash:
        if NumHash[i] == n:
            print(i)