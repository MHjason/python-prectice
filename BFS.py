#%%
maze = [ ["#","S","#","#","#"],
         [".",".",".","#","#"],
         [".","#",".",".","."],
         [".","#",".","#","#"],
         [".","#",".",".","#"],
         [".",".","#","G","#"]]
#%%
import queue
q = queue.Queue()
D = []
INF = 1000000
sx, sy = 0, 1
gx, gy = 5, 3
d =[[0]*len(maze[1]) for i in range(len(maze))]
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

def bfs():
    for i in range(len(maze)):
        for j in range(len(maze[1])):
            d[i][j] = INF
    q.put([sx,sy])
    d[sx][sy] = 0
    
    while (q.empty() != True):
        D = q.get()
        if D[0] == gx and D[1] == gy:
            break
        for i in range(4):
            nx = D[0] + dx[i]
            ny = D[1] + dy[i]
            if 0 <= nx and nx < len(maze) and 0<=ny and ny < len(maze[1]) and maze[nx][ny] != "#" and d[nx][ny] == INF :
                q.put([nx, ny])
                d[nx][ny] = d[D[0]][D[1]] + 1
    return d[gx][gy]

#%%
res = bfs()
#============分隔線===========================================
#%%
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

#%%
class Solution:
    def isSameTree(self, p, q):
        from collections import deque
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        queue = [(p,q)]
        while queue:
            p,q = queue.pop(0)
            if not p and not q:
                continue
            if (p or q) and not (p and q):
                return False
            if p.val != q.val:
                return False
            queue.append((p.left,q.left))
            queue.append((p.right,q.right))
        return True

# %%=========python 不需break return後會自動break
def A():
    S = [(1,1),(1,1),(1,1),(1,1),(1,1),(1,1),(1,1)]
    while S:
        print(S)
        S.pop(0)
        return False
A()
#============分隔線===========================================
