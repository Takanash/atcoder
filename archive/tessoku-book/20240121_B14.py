import sys
import bisect

DEBUG=True
TIME=False

def main():
  N, K = [int(i) for i in input().split(' ')]
  A = [int(i) for i in input().split(' ')]

  # Aを半分に分け、ビット全探索で取りうるカードの合計を出す
  A1 = A[:len(A)//2]
  A2 = A[len(A)//2:]
  B1 = bitwise_binary_search(A1)
  B2 = bitwise_binary_search(A2)
  B1.sort()
  B2.sort()

  for i in range(len(B1)):
    index = bisect.bisect_left(B2, K-B1[i])
    if index < len(B2) and B2[index] == K - B1[i]:
      print('Yes')
      sys.exit(0)
  
  print('No')


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
