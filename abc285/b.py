# https://atcoder.jp/contests/abc285/tasks/abc285_b

N = int(input())
S = input()

for i in range(1, N):
    ans = [0]
    first_index = 1
    second_index = 1 + i
    while True:
        if second_index > N or S[first_index - 1] == S[second_index - 1]:
            break
        ans.append(first_index)
        first_index += 1
        second_index = first_index + i
    print(max(ans))
