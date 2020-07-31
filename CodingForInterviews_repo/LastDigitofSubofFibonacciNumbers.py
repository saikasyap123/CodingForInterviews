def fun2(n):
    previous_ = 0
    current_ = 1
    sum_ = 1
    for i in range(2,n+1):
        next_ = previous_ + current_
        sum_= sum_ + next_
        previous_ = current_
        current_ = next_
    return sum_ % 10
    
    
n = int(input("enter the length of fibonacci series:"))
print('last digit of sum of fibonacci numbers is {}'.format(fun2(n)))