n = int(input())
for i in range(n):
    sum = 0
    str_list = list(input())
    for j in range(len(str_list)):
        if str_list[j] == '(':
            sum += 1
        elif str_list[j] == ')':
            sum -= 1
        if sum <0:
            print("NO")
            break
    if sum >0:
        print("NO")
    elif sum == 0:
        print("YES")
