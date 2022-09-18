
# palindrome number check
# 121 == palindrome**

def palindrome(x):
    if(x<0):
        return False
    
    i = x
    s = 0

    while(i>0):
        div = i % 10
        s = s* 10 + div
        i = i // 10
    if(x == s):
        return True
    return False

print(palindrome(121))