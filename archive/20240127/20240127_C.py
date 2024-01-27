import sys

DEBUG=False
TIME=False

def main():
  n = int(input())
  Q = [int(i) for i in input().replace('\n', '').split(' ')]
  A = [int(i) for i in input().replace('\n', '').split(' ')]
  B = [int(i) for i in input().replace('\n', '').split(' ')]

  a_max = min([int(Q[i] / A[i]) if A[i] != 0 else float('inf') for i in range(n)])
  b_max = min([int(Q[i] / B[i]) if B[i] != 0 else float('inf') for i in range(n)])

  max = 0
  # Aは全探索
  for i in reversed(range(a_max+1)):
    b_l = 0
    b_r = b_max
    b_index_max = 0

    # Bは二分探索
    while b_l <= b_r:
      isOver = False
      mid = int((b_l + b_r)/ 2)
      for j in range(n):
        if (A[j] * i + B[j] * mid) > Q[j]:
          isOver = True
          break
      else:
        b_index_max = mid
      # print(f'i: {i}, b_l: {b_l}, b_r: {b_r}, mid: {mid}, b_index_max: {b_index_max}, max: {max}')
      if isOver:
        b_r = mid - 1
      else:
        b_l = mid + 1
      
    if b_index_max + i > max:
      max = b_index_max + i
    
  print(max)



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
