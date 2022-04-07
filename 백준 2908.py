
a,b = list(input().split())

def rev(num1):
    num1 = list(num1)
    tmp=num1[0]
    num1[0]=num1[2]
    num1[2]=tmp
    num2 = ''.join(num1)
    return (int(num2))

a_rev = rev(a)
b_rev = rev(b)
print(max(a_rev,b_rev))
