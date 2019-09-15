from collections import deque

map_lst = []
for loop in range(12):
    map_lst.append(list(map(str, input())))

dy = [-1, 0, 1, 0]
dx = [0, -1, 0, 1]
flag = True
ans = 0
while flag:
    flag = False
    visited = [[0] * 6 for loop in range(12)]
    for y in range(12):
        for x in range(6):
            if map_lst[y][x] != '.' and visited[y][x] == 0:
                queue = deque()
                queue.append([y, x, map_lst[y][x]])
                visited[y][x] = 1
                temp = [[y,x]]
                while queue:
                    cur = queue.popleft()
                    for dir in range(4):
                        next_y = cur[0] + dy[dir]
                        next_x = cur[1] + dx[dir]
                        if 0 <= next_y < 12 and 0 <= next_x < 6:
                            if visited[next_y][next_x] == 0:
                                if map_lst[next_y][next_x] == cur[2]:
                                    temp.append([next_y, next_x])
                                    queue.append([next_y, next_x, cur[2]])
                                    visited[next_y][next_x] = 1
                if len(temp) >= 4:
                    for data in temp:
                        map_lst[data[0]][data[1]]='.'
                    flag = True

    for re_x in range(6):
        for re_y in range(11,-1,-1):
            if map_lst[re_y][re_x]!='.':
                for re_y2 in range(11,re_y-1,-1):
                    if map_lst[re_y2][re_x]=='.':
                        map_lst[re_y2][re_x]=map_lst[re_y][re_x]
                        map_lst[re_y][re_x]='.'

    if flag == True:
        ans += 1
print(ans)