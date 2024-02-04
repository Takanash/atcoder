import sys

DEBUG=False
TIME=False

def main():
  # 数値Nを取得する場合
  N = int(input())
  # 数値N, Xを取得する場合
  N, X = [int(i) for i in input().split(' ')]
  # 1行の空白文字で分割された数値を配列Sとして取得する場合
  S = [int(i) for i in input().split(' ')]
  # N行の数値の配列Aを取得する場合
  A = [int(input()) for _ in range(N)]
  # N 行の `L R` を二次元配列[[L1, R1], ...]として取得する場合 
  L_R = [list(map(int, input().split(' '))) for _ in range(N)]



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
