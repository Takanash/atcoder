import sys
import time

def main():
  input = sys.stdin.readline
  # 数値 n を取得する場合
  n = int(input())
  # 数値 n, x を取得する場合
  n, x = map(int, input().replace('\n', '').split(" "))
  # 文字列 s を取得する場合
  s = input()
  # 1行に n 個ある数値を配列 s として取得する場合
  s = map(int, input().replace('\n', '').split(" "))
  # n 行の数値の配列 a を取得する場合
  a = []
  for i in range(n):
    a.append(input().replace('\n', '').split(" "))


# start = time.time()

if __name__ == '__main__':
  main()

# end = time.time()
# time_diff = end - start
# print(f"実行時間: {str(time_diff)}")
