# https://atcoder.jp/contests/abc032/tasks/abc032_a

a, b, n = [int(input()) for _ in range(3)]
while not (n % a == 0 and n % b == 0):
    n += 1
print(n)
