def permution(arr, M): #수열 만들어주는 함수
    used = [0 for _ in range(len(arr))]#사용 유무 확인을 위한 리스트만들어줌

    def generate(choose, used):#하나씩 만들어주는 함수
        if len(choose) == M:#M개의 원소가 담긴 수엶이 만들어진다면
            print(' '.join(choose))#문자열로 변환해서 출력
            return

        for i in range(len(arr)):#for문돌면서 한개씩 넣어줌
            if not used[i]:#사용하지 않았다면
                choose.append(str(arr[i]))#choose에 str형변환 후 넣어줌
                used[i] = 1#사용표시 해주기
                generate(choose, used)#재귀로 돌면서 넣어줌
                choose.pop()#더이상 갈 곳이 없으니 빼주고
                used[i] = 0#사용유무도 갱신

    generate([], used)


N, M = map(int, input())#입력받아오기
arr = []#원소가 담긴 리스트 만들어줌
for i in range(1, N + 1):
    arr.append(i)
permution(arr, M)