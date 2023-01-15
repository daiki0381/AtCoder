# https://atcoder.jp/contests/abc285/tasks/abc285_c

"""
ALLの場合
(26 ** 2) * 1 + (26 ** 1) * 12 + (26 ** 0) * 12 => 1000
"""

def convert_alpha_to_num(alpha):
    num = 0
    for index, item in enumerate(list(alpha)):
        num += pow(26, len(alpha) - index - 1) * (ord(item) - ord("A") + 1)
    return num

print(convert_alpha_to_num(input()))
