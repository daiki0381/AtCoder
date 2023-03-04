# https://atcoder.jp/contests/abc292/tasks/abc292_b

from collections import defaultdict

N, Q = map(int, input().split())
d = defaultdict(str)

for _ in range(Q):
    c, x = map(int, input().split())
    if c == 1:
        if d[x] == "レッドカード":
            continue
        elif d[x] == "イエローカード":
            d[x] = "レッドカード"
        else:
            d[x] = "イエローカード"
    elif c == 2:
        d[x] = "レッドカード"
    else:
        if d[x] == "レッドカード":
            print("Yes")
        else:
            print("No")
