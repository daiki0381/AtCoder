# https://atcoder.jp/contests/abc291/tasks/abc291_b

N = int(input())
X = sorted(list(map(int, input().split())))

for _ in range(N):
    X.pop()
    X.pop(0)

print(sum(X) / len(X))
