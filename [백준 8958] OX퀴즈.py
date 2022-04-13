N = int(input())
for i in range(N):
    result = input()
    cnt = 0
    sum = 0
    for idx in range(len(result)):
        if result[idx] == "O":
            cnt += 1
            sum += cnt
        else:
            cnt = 0
    print(sum)