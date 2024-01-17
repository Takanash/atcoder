import sys

DEBUG=False
TIME=False

def main():
  n, k = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  count = 0
  r = 0
  dp = []
  for l in range(n):
    while r < n:
      # print(f'l: {l}, r: {r}, dp: {dp}, sum(a[l:r+1]: {sum(a[l:r+1])}')
      if sum(a[l:r+1]) > k:
        r -= 1
        break
      else:
        count += 1
        r += 1
    dp.append(count)
    count = r - l - 1

  print(sum(dp))


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
