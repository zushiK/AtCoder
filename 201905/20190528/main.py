# Guidebook https://atcoder.jp/contests/abc128/tasks/abc128_b

N = int(input())

P = [[0 for i in range(3)] for j in range(N)]

for i in range(N):
    P[i][0],P[i][1]  = input().split()
    P[i][1] = 100 - int(P[i][1])
    P[i][2] = i + 1

P.sort()

for i in range(N):
    print(P[i][2])
