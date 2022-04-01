#백준 2667번 단지번호
#dfs풀이

n = int(input()) #배열 개수 입력 받고
map = [list(map(int,input())) for _ in range(n)] #배열 입력받기
home_list = [] #단지가 몇개인지 세주기 위해
cnt = 0#단지안에 집 몇개인지 세주기위해

#좌표 위아래좌우
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    global cnt#전역변수 사용을 위해
    num = len(map)#범위 지정을 위해
    if x<0 or y < 0 or x>= num or y>= num:#x,y가 범위밖에있을때
        return False

    if map[x][y] == 1:#집이 있을때
        map[x][y] = 0#방문해줬으니까 0으로 바꿔주고
        cnt += 1#집+1해줌
        for i in range(4):#위아래좌우로 움직여서 이동
            dfs(x+dx[i],y+dy[i])
        return True#단지 한개 탐색완료


for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            home_list.append(cnt)#단지 한개 탐색후 집 개수 넣어줌
            cnt = 0 #다음 단지 탐색을 위해 다시 cnt 0으로 초기화

home_list.sort() #오름차순 정렬을위해
print(len(home_list))#단지개수
for i in range(len(home_list)):#단지마다 집개수 
    print(home_list[i])