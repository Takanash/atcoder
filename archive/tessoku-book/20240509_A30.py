import sys
import math

DEBUG=True
TIME=False

def main():
  N, R = [int(i) for i in input().split(' ')]
  wari = 1000000007

  fac_n = math.factorial(N)
  fac_r = math.factorial(R)
  fac_n_r = math.factorial(N-R)
  top = fac_n % wari
  bottom = (fac_r * fac_n_r) % wari

  print((top * pow(bottom, wari-2, wari)) % wari)



# 標準エラー出力に引数を出力する
# デバッグ用
def error(*args, end="\n"):
  print(*args, end=end, file=sys.stderr)


# 10進数→n進数への変換
# CAUTION: 11進数以上は変換不可
# @param [int] value 変換する値
# @param [int] base 変換するn進数
# @return [str] n進数に変換した値
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


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
