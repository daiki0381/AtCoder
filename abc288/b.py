# https://atcoder.jp/contests/abc288/tasks/abc288_b

N, K = map(int, input().split())
handle_names = []

for _ in range(N):
    S = input()
    if len(handle_names) < K:
        handle_names.append(S)

for handle_name in sorted(handle_names):
    print(handle_name)
