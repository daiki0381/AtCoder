# https://atcoder.jp/contests/abc291/tasks/abc291_a.

S = input()
ans = 0

for s in S:
    ans += 1
    if s.isupper():
        print(ans)
