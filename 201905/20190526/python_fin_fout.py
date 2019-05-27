# ファイル読み取り

# f = open('./ans1.txt')
# data1 = f.read()
# f.close()

# input().splint()で標準入力のくぎりを行う。map(int)でString型からintがたに変換し
# N,Kに代入
N, K = map(int, input().split())

S = input()

result = S[:K-1] + S[K-1].lower() + S[K:]
print(result)