import sys

DEBUG=False
TIME=False

def main():
  h, w, k = [int(i) for i in input().replace('\n', '').split(' ')]
  s = [list(input().replace('\n', '')) for i in range(h)]

  min = float('inf')
  for y in range(h):
    dot_count = 0
    dot_and_circle_count = 0
    for x in range(w):
      if s[y][x] == '.':
        dot_count += 1
        dot_and_circle_count += 1
      elif s[y][x] == 'o':
        dot_and_circle_count += 1
      else:
        dot_count = 0
        dot_and_circle_count = 0

      if dot_and_circle_count == k:
        if x-k >= 0 and s[y][x-k] == '.':
          dot_count -= 1
        if dot_count < min:
          min = dot_count
        dot_and_circle_count -= 1

  for x in range(w):
    dot_count = 0
    dot_and_circle_count = 0
    for y in range(h):
      if s[y][x] == '.':
        dot_count += 1
        dot_and_circle_count += 1
      elif s[y][x] == 'o':
        dot_and_circle_count += 1
      else:
        dot_count = 0
        dot_and_circle_count = 0

      if dot_and_circle_count == k:
        if y-k >= 0 and s[y-k][x] == '.':
          dot_count -= 1
        if dot_count < min:
          min = dot_count
        dot_and_circle_count -= 1
  
  if min == float('inf'):
    print('-1')
  else:
    print(min)



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
