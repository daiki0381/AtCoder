# https://atcoder.jp/contests/abc289/tasks/abc289_c

from itertools import product

N, M = map(int, input().split())
nested_s_list = []
ans = 0
from_one_to_n_list = set()
for i in range(1, N + 1):
    from_one_to_n_list.add(i)

for _ in range(M):
    C = int(input())
    s_list = list(map(int, input().split()))
    nested_s_list.append(s_list)

nested_use_list = list(product([0, 1], repeat=M))

for use_list in nested_use_list:
    ans_list = set()
    for i, use in enumerate(use_list):
        if use == 1:
            for s in nested_s_list[i]:
                ans_list.add(s)
    if ans_list == from_one_to_n_list:
        ans += 1

print(ans)
