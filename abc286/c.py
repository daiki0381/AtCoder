N, A, B = map(int, input().split())
S = input()

if N == 1 or S == S[::-1]:
    print(0)
    exit()

ans_list = set()

for i in range(N):
    ans = 0
    if i != 0:
        S = S[1:N] + S[0]
        ans += i * A
    half = N // 2
    if N % 2 == 0:
        left = list(S[0:half])
        right = list(S[half:N])[::-1]
        for j in range(len(left)):
            if left[j] != right[j]:
                ans += B
    else:
        left = list(S[0:half])
        right = list(S[half + 1 : N])[::-1]
        for j in range(len(left)):
            if left[j] != right[j]:
                ans += B
    ans_list.add(ans)

print(min(ans_list))
