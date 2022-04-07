def dfs(idx,result):
    #promise 부분 들어가야됨 연산을 다 돌았는지 확인
    global min_val,max_val
    if idx == N-1:
        if result <= min_val:
            min_val = result
        if result >= max_val:
            max_val = result
        return

    for i in range(4):#연산자가4개니까 4번돌음 (인덱스가 0,1,2,3에 각각다른 연산자가 들어 있으므로)
        if op[i] > 0:#각 인덱스의 여분이 있으면
            op[i] -= 1#사용해줌
            if i == 0:
                new_result = result + num[idx+1]
            elif i == 1:
                new_result = result - num[idx+1]
            elif i == 2:
                new_result = result * num[idx+1]
            else:
                new_result = int(result/num[idx+1])
            dfs(idx+1,new_result)
            op[i] += 1#백트레킹을 위해서 다시 원상복귀해줌 


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    op = list(map(int,input().split()))
    num = list(map(int, input().split()))
    max_val = -999999999
    min_val = 999999999
    dfs(0,num[0])
    print("#{} {}".format(tc,max_val-min_val))
