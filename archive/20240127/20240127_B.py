import sys

DEBUG=False
TIME=False

def main():
  s = input().replace('\n', '')
  arr = [0 for _ in range(26)]
  diff = 97

  for c in s:
    arr[ord(c) - diff] += 1

  index = -1
  max = 0
  for i, n in enumerate(arr):
    if max < n:
      index = i
      max = n
  
  print(chr(index+diff))
  


# 10進数→n進数への変換
# @param [int] value 変換する値
# @param [int] base 変換するn進数
# @return [str] n進数に変換した値
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


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
