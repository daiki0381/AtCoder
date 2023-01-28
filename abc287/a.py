# https://atcoder.jp/contests/abc287/tasks/abc287_a

N = int(input())
S = [input() for _ in range(N)]
half = N // 2
for_num = 0

for s in S:
    if s == "For":
        for_num += 1

if half < for_num:
    print("Yes")
else:
    print("No")
