import sys
import math

DEBUG=False
TIME=False

def main():
  q = int(input())
  x = [int(input()) for i in range(q)]

  for i in x:
    sqrt_x = int(math.sqrt(i))
    for j in range(2, sqrt_x+1):
      if i % j == 0:
        print('No')
        break
    else:
      print('Yes')


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
