#백준 2667번 단지번호
#bfs풀이

from collections import deque#que사용을 위해

n = int(input()) #배열 개수 입력 받고
map = [list(map(int,input())) for _ in range(n)] #배열 입력받기
home_list = [] #단지가 몇개인지 세주기 위해


#좌표 위아래좌우
dx=[-1,1,0,0]
dy=[0,0,1,-1]

def bfs(map,x,y):
    q = deque()#deque선언
    num = len(map)#범위 지정을 위해
    q.append((x,y))#큐에 넣어주고
    cnt =1#처음 map[x][y]==1이니까 초기화를 1로해줌

    while q:
        x,y = q.popleft()#하나씩 꺼내서 탐색
        for i in range(4):#위아래좌우탐색
            nx = x+dx[i]
            ny = y+dy[i]
            if nx<0 or ny < 0 or nx>= num or ny>= num:#x,y가 범위밖에있을때
                continue

            if map[nx][ny] == 1:#집이 있을때
                map[nx][ny] = 0#방문해줬으니까 0으로 바꿔주고
                q.append((nx,ny))#큐에 삽입
                cnt += 1#집+1해줌
    return cnt



for i in range(n):
    for j in range(n):
        if map[i][j] == 1:
            map[i][j] = 0
            home_list.append(bfs(map,i,j))


home_list.sort() #오름차순 정렬을위해
print(len(home_list))#단지개수
for i in range(len(home_list)):#단지마다 집개수
    print(home_list[i])