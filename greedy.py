#%%
V = [1,5,10,50,100,500]
C = [3,2,1,3,0,2]
A = 620
ans = 0

for i in range(6):
    t = min(A//V[5-i], C[5-i])
    A -= t*V[5-i]
    ans += t
print(ans)

#=======================分隔線===========
# %%
n = 5
s = [1, 2, 4, 6, 8, 10, 13, 14, 21]
t = [3, 5, 7, 9, 11, 12, 15, 19, 23]
F = 0
ans = 0

for i in range(len(t)):
    if F < s[i]: 
        F = t[i]
        ans += 1
print(ans)

#=======================分隔線===========


# %%
def maximum69Number (num):
    j = 0
    num_str = str(num)
    for i in num_str:
        if i == '6':
            num = num + 3*(10**(3-j))
            break
        j += 1
    return num
# %%
maximum69Number(9669)
# %%
