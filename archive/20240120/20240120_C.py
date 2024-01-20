import sys

DEBUG=True
TIME=False

# TLE
# https://atcoder.jp/contests/abc337/submissions/49508724 を元に回答作成
def main():
  # 数値 n を取得する場合
  n = int(input())
  a = tuple([int(i) for i in input().replace('\n', '').split(' ')])

  arr = [0 for i in range(n+2)]
  for i, x in enumerate(a):
    arr[x] = i + 1
  
  l = [a.index(-1) + 1]

  for _ in range(n-1):
    l.append(arr[l[-1]])

  print(*l)



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
  print(f"実行時間: {str(time_diff)}")


# 10進数→n進数への変換
# @param [int] value 変換する値
# @param [int] base 変換するn進数
# @return [str] n進数に変換した値
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)
