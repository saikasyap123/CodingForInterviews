def f2(string):
    validation_set = {'}':'{',')':'(',']':'['}
    push_arr = []
    for i in string:
        if i=='{' or i=='(' or i=='[':
            push_arr.append(i)
        elif i in validation_set:
            if validation_set[i]==push_arr[len(push_arr)-1]:
                push_arr.pop()
            else:
                return False
    return True
                
    
n = input('Enter the string:')
print(f2(n))