def f1(s):
    if s == s[::-1]:
        return True
    else :
        return False

n = input("Enter the string:")
p=0
q=p+1
max_len = 0
final_string = ""
while p < len(n):
    
    q = p+1
    while q < len(n):
            
            t = f1(n[p:q+1])
            if t :
               if max_len<(q-p+1):
                    max_len =(q-p+1)
                    final_string = n[p:q+1]
                
            q +=1
    p +=1
print("largest palindromic substring in the given string is {}".format(final_string))
    