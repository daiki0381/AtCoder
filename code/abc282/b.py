# https://atcoder.jp/contests/abc282/tasks/abc282_b

N, M = map(int, input().split())
S = [input() for _ in range(N)]
pairs = []
for i in range(1, N + 1):
    for n in range(1, N + 1):
        if i != n:
            pairs.append(tuple(sorted([i, n])))
pairs = sorted(list(set(pairs)))
ans = 0
for pair in pairs:
    solved_num = 0
    for m in range(1, M + 1):
        if S[pair[0] - 1][m - 1] == "o" or S[pair[1] - 1][m - 1] == "o":
            solved_num += 1
        if solved_num == M:
            ans += 1
print(ans)
