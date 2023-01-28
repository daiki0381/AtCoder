# https://atcoder.jp/contests/abc287/tasks/abc287_c

from collections import deque, defaultdict

N, M = map(int, input().split())
d = defaultdict(list)

# 次数が1つの数
degree_1 = 0
# 次数が2つの数
degree_2 = 0
# 連結成分の数
connected_component_num = 0

for _ in range(M):
    a, b = map(int, input().split())
    d[a].append(b)
    d[b].append(a)

for k, v in d.items():
    if len(v) == 1:
        degree_1 += 1
    elif len(v) == 2:
        degree_2 += 1

que = deque()
seen = set()
for i in range(1, N + 1):
    if i not in seen:
        connected_component_num += 1
        que.append(i)
        while que:
            now = que.popleft()
            for i in d[now]:
                if i not in seen:
                    que.append(i)
                    seen.add(i)

if degree_1 == 2 and degree_2 == N - 2 and connected_component_num == 1:
    print("Yes")
else:
    print("No")
