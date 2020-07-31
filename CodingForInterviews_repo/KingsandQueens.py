def k_q(h1, h2, h3, h4):
    if (1<=h1<=8 and 1<=h2<=8 and 1<=h3<=8 and 1<=h4<=8):
        if h1==h3 or h2==h4 or abs(h1-h3)==abs(h2-h4):
            return True
        else :
            return False
    else :
        return 'Invalid Input'

tokens = input().split()
cor_Array = [int(x) for x in tokens]
print(k_q(cor_Array[0], cor_Array[1], cor_Array[2], cor_Array[3]))