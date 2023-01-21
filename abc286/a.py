# https://atcoder.jp/contests/abc286/tasks/abc286_a

N, P, Q, R, S = map(int, input().split())
A = list(map(int, input().split()))
A[P - 1 : Q], A[R - 1 : S] = A[R - 1 : S], A[P - 1 : Q]
print(*A)
