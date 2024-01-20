import sys

DEBUG=False
TIME=False

def main():
  n = int(input())
  x_y = [list(map(int, input().replace('\n', '').split(' '))) for i in range(n)]

  x_sum = 0
  y_sum = 0
  for x, y in x_y:
    x_sum += x
    y_sum += y

  if x_sum == y_sum:
    print('Draw')
  elif x_sum > y_sum:
    print('Takahashi')
  else:
    print('Aoki')



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
