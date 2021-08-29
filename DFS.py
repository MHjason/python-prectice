#%%
a = [1,2,4,7]
k = 15
n = 4
def dfs(sum , i):
    if i == n:
        return sum == k
    if dfs(sum , i+1):
        return True
    if dfs(sum + a[i], i+1):
        return True
    return False
#=========
if dfs(0, 0):
    print("True")
else:
    print("false")

#====================分隔線===================
#%%
field = [["w",".",".","W","W"],
         ["w",".",".","W","W"],
         ["w",".",".",".","."],
         [".",".","W",".","."],
         [".","W",".","W","."],
         [".",".","W",".","."]]
N = 6
M = 5
def dfs(col, row):
    field[col][row] = "."
    for i in range(-1,1,1):
        for j in range(-1,1,1):
            nx = col + i
            ny = row + j
            if field[i][j] == "w" and nx < N and ny < M and nx >= 0 and ny >= 0:
                dfs(nx, ny)
    return             

# ==========
res = 0
for i in range(N):
    for j in range(M):
        if field[i][j] == "w":
            dfs(i,j)
            res += 1
print(res)
#================分隔線================

