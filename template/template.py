import sys

DEBUG=False
TIME=False

def main():
  # 数値 n を取得する場合
  n = int(input())
  # 文字列 s を取得する場合
  s = input()
  # 数値 n, x を取得する場合
  n, x = [int(i) for i in input().replace('\n', '').split(' ')]
  # 1行に n 個ある数値を配列 s として取得する場合
  s = [int(i) for i in input().replace('\n', '').split(' ')]
  # n 行の数値の配列 a を取得する場合
  a = [int(input()) for _ in range(n)]
  # n 行の `l r` を二次元配列[[l1, r1], ...]として取得する場合 
  l_r = [list(map(int, input().replace('\n', '').split(' '))) for _ in range(n)]



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
