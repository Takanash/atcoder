import sys

DEBUG=False
TIME=False

def main():
  h, w, n = [int(i) for i in input().split(' ')]
  arr = [['.' for _ in range(w)] for _ in range(h)]

  x = 0
  y = 0
  direction = 'u'
  for _ in range(n):
    color = arr[y][x]
    if color == '.':
      arr[y][x] = '#'
      if direction == 'u':
        direction = 'r'
        x += 1
        if x >= w:
          x = 0
      elif direction == 'r':
        direction = 'd'
        y += 1
        if y >= h:
          y = 0
      elif direction == 'd':
        direction = 'l'
        x -= 1
        if x < 0:
          x = w-1
      else: 
        direction = 'u'
        y -= 1
        if y < 0:
          y = h-1
    else:
      arr[y][x] = '.'
      if direction == 'u':
        direction = 'l'
        x -= 1
        if x < 0:
          x = w-1
      elif direction == 'l':
        direction = 'd'
        y += 1
        if y >= h:
          y = 0
      elif direction == 'd':
        direction = 'r'
        x += 1
        if x >= w:
          x = 0
      else:
        direction = 'u'
        y -= 1
        if y < 0:
          y = h-1
  
  for a in arr:
    for c in a:
      print(c, end='')
    print()


# 標準エラー出力に引数を出力する
# デバッグ用
def error(*args, end="\n"):
  print(*args, end=end, file=sys.stderr)


# 10進数→n進数への変換
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
