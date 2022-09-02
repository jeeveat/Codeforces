n = int(input())
s = input()
res = [[0 for j in range(0, n)]for i in range(0, n)]
for l in range(n-1, -1,-1):
    for r in range(l,n):
        if l == r:
            res[l][r] = 1
        else:
            res[l][r] = 1 + res[l+1][r]
            for m in range(l+1,r + 1):
                if s[l]==s[m]:
                    res[l][r] = min(res[l][r], res[l+1][m-1] + res [m][r]) 

print(res[0][n-1])
