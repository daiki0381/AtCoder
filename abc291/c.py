# https://atcoder.jp/contests/abc291/tasks/abc291_c

N = int(input())
S = input()
coordinates = [(0, 0)]

for s in S:
    if s == "R":
        x = coordinates[-1][0] + 1
        y = coordinates[-1][1]
        coordinates.append((x, y))
    elif s == "L":
        x = coordinates[-1][0] - 1
        y = coordinates[-1][1]
        coordinates.append((x, y))
    elif s == "U":
        x = coordinates[-1][0]
        y = coordinates[-1][1] + 1
        coordinates.append((x, y))
    elif s == "D":
        x = coordinates[-1][0]
        y = coordinates[-1][1] - 1
        coordinates.append((x, y))


def is_duplicate(list):
    return len(list) != len(set(list))


if is_duplicate(coordinates):
    print("Yes")
else:
    print("No")
