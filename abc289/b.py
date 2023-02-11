# https://atcoder.jp/contests/abc289/tasks/abc289_b

N, M = map(int, input().split())
a_list = list(map(int, input().split()))
p_list = [i for i in range(1, N + 1)]
nested_a_list = []
tmp_list = []

for a in a_list:
    if a_list.count(a + 1) != 0:
        tmp_list.append(a)
    else:
        tmp_list.append(a)
        nested_a_list.append(tmp_list)
        tmp_list = []

for a_list in nested_a_list:
    if len(a_list) == 1:
        p_list[a_list[0]], p_list[a_list[0] - 1] = (
            p_list[a_list[0] - 1],
            p_list[a_list[0]],
        )
    elif len(a_list) != 1:
        p_list[a_list[0] - 1 : a_list[-1] + 1] = p_list[a_list[0] - 1 : a_list[-1] + 1][
            ::-1
        ]

print(*p_list)
