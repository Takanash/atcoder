import sys

def main():
  # 提出用
  # input = sys.stdin.readline
  # デバッグ用（提出時に使うと遅い可能性あり）
  if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
  # 数値 n を取得する場合
  n = int(input())
  # 文字列 s を取得する場合
  s = input()
  # 数値 n, x を取得する場合
  n, x = [int(i) for i in input().replace('\n', '').split(' ')]
  # 1行に n 個ある数値を配列 s として取得する場合
  s = [int(i) for i in input().replace('\n', '').split(' ')]
  # n 行の数値の配列 a を取得する場合
  a = [input() for i in range(n)]
  # n 行の `l r` を二次元配列[[l1, r1], ...]として取得する場合 
  l_r = [list(map(int, input().replace('\n', '').split(' '))) for i in range(n)]



# 時間計測用
# import time
# start = time.time()

if __name__ == '__main__':
  main()

# end = time.time()
# time_diff = end - start
# print(f"実行時間: {str(time_diff)}")
