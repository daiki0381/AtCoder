# https://atcoder.jp/contests/abc249/tasks/abc249_a

A, B, C, D, E, F, X = map(int, input().split())
if X % (A + C) == 0:
    takahashi = X // (A + C) * A * B
else:
    if X < A + C:
        if X < A:
            takahashi = X * B
        else:
            takahashi = A * B
    else:
        if X % (A + C) > A:
            takahashi = X // (A + C) * A * B + A * B
        else:
            takahashi = X // (A + C) * A * B + ((X % (A + C)) * B)

if X % (D + F) == 0:
    aoki = X // (D + F) * D * E
else:
    if X < D + F:
        if X < D:
            aoki = X * E
        else:
            aoki = D * E
    else:
        if X % (D + F) > D:
            aoki = X // (D + F) * D * E + D * E
        else:
            aoki = X // (D + F) * D * E + ((X % (D + F)) * E)

if aoki > takahashi:
    print("Aoki")
elif aoki < takahashi:
    print("Takahashi")
else:
    print("Draw")
