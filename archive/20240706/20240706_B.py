import sys

DEBUG=False
TIME=False

# WA
def main():
  a, b, c, d, e, f = [int(i) for i in input().replace('\n', '').split(' ')]
  g, h, i, j, k, l = [int(i) for i in input().replace('\n', '').split(' ')]

  flg = False

  if is_coordinate_into_cube(a, b, c, d, e, f, g, h, i) or \
     is_coordinate_into_cube(a, b, c, d, e, f, j, h, i) or \
     is_coordinate_into_cube(a, b, c, d, e, f, g, k, i) or \
     is_coordinate_into_cube(a, b, c, d, e, f, j, k, i) or \
     is_coordinate_into_cube(a, b, c, d, e, f, g, h, l) or \
     is_coordinate_into_cube(a, b, c, d, e, f, j, h, l) or \
     is_coordinate_into_cube(a, b, c, d, e, f, g, k, l) or \
     is_coordinate_into_cube(a, b, c, d, e, f, j, k, l):
      flg = True
  elif g <= a < d <= j:
    if is_coordinate_into_plane(b, c, e, f, h, i) or \
       is_coordinate_into_plane(b, c, e, f, h, k) or \
       is_coordinate_into_plane(b, c, e, f, j, i) or \
       is_coordinate_into_plane(b, c, e, f, j, k):
      flg = True
  elif h <= b < e <= k:
    if is_coordinate_into_plane(a, c, d, f, g, i) or \
       is_coordinate_into_plane(a, c, d, f, g, l) or \
       is_coordinate_into_plane(a, c, d, f, j, i) or \
       is_coordinate_into_plane(a, c, d, f, j, l):
      flg = True
  elif i <= c < f <= l:
    if is_coordinate_into_plane(a, b, d, e, g, h) or \
       is_coordinate_into_plane(a, b, d, e, g, k) or \
       is_coordinate_into_plane(a, b, d, e, j, h) or \
       is_coordinate_into_plane(a, b, d, e, j, k):
      flg = True
  elif a == g and b == h and c == i and d == j and e == k and f == l:
    flg = True

  if flg:
    print('Yes')
  else:
    print('No')

def is_coordinate_into_cube(a, b, c, d, e, f, x, y, z):
  return a < x < d and b < y < e and c < z < f

def is_coordinate_into_plane(a, b, c, d, x, y):
  return a < x < c and b < y < d


# 標準エラー出力に引数を出力する
# デバッグ用
def error(*args, end="\n"):
  print(*args, end=end, file=sys.stderr)


# 10進数→n進数への変換
# CAUTION: 11進数以上は変換不可
# @param [int] value 変換する値
# @param [int] base 変換するn進数
# @return [str] n進数に変換した値
def decimal_to_base(value, base):
    if (int(value / base)):
        return decimal_to_base(int(value / base), base) + str(value % base)
    return str(value % base)


# n進数→10進数への変換
# CAUTION: 11進数以上は変換不可
# @param [str] value 変換する値
# @param [int] base valueのn進数
# @return [str] 10進数に変換した値
def base_to_decimal(value, base):
  sum = 0
  for i, c in enumerate(reversed(value)):
    sum += int(c) * base ** i
  return sum


# ビット全探索
# 引数の配列の数値の和であり得る組み合わせ全てを返す
# @param [list] arr 数値の配列
# @return [list] あり得る組み合わせの配列
def bitwise_binary_search(arr):
  sum_list = []
  for i in range(2 ** len(arr)):
    sum = 0 # 現在の合計値
    for j in range(len(arr)):
      wari = (2 ** j)
      if (i // wari) % 2 == 1:
        sum += arr[j]
    sum_list.append(sum)
  return sum_list


# ユークリッドの互除法
# 2つの数値の最大公約数を求める
# math.gcd(a, b) でもよい
# @param [int] a 数値
# @param [int] b 数値
# @return [int] 最大公約数
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

# 2つの数値の最小公倍数を求める
# math.lcm(a, b) でもよい
# @param [int] a 数値
# @param [int] b 数値
# @return [int] 最小公倍数
def lcm(a, b):
  return a * b // gcd(a, b)


# 繰り返し二乗法
# a**bをmで割った余りを計算量O(log m)で出す
# pow(a, b, m)でも良い
def power(a, b, m):
  p = a
  ans = 1
  for i in range(30):
    wari = 2**i
    # Bを2進数と考えてA^Bを分解する
    # 例えば5^23 = 5^1 * 5^2 * 5^4 * 5^16
    if (b//wari) % 2 == 1:
      ans = (ans * p) % m
    p = (p * p) % m
  return ans


# 引数の配列のニム和（XORの和）を返す
# @param [list] arr ニム和を求める配列
# @return [int] ニム和
def nim_sum(arr):
  sum = arr[0]
  for a in arr[1:]:
    sum = sum ^ a
  return sum


if TIME:
  import time
  start = time.time()

if DEBUG:
  if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
else:
  input = sys.stdin.readline


if __name__ == '__main__':
  main()

if TIME:
  end = time.time()
  time_diff = end - start
  error(f"実行時間: {str(time_diff)}")
