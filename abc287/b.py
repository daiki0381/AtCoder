# https://atcoder.jp/contests/abc287/tasks/abc287_b

N, M = map(int, input().split())
S = [input() for _ in range(N)]
T = [input() for _ in range(M)]
ans = 0

for s in S:
    is_found = False
    for t in T:
        if s[3:6] == t:
            is_found = True
    if is_found:
        ans += 1

print(ans)
