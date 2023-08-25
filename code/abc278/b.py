# https://atcoder.jp/contests/abc278/tasks/abc278_b

H, M = input().split()
A, B = H.zfill(2)
C, D = M.zfill(2)
while True:
    if int(A + C) <= 23 and int(B + D) <= 59:
        print(A + B, C + D)
        break
    if int(C + D) == 59:
        C, D = "0", "0"
        if int(A + B) == 23:
            A, B = "0", "0"
        else:
            new_a_b = int(A + B) + 1
            A, B = str(new_a_b).zfill(2)
    else:
        new_c_d = int(C + D) + 1
        C, D = str(new_c_d).zfill(2)
