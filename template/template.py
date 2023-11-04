import sys

def main():
  input = sys.stdin.readline
  # 数値 n を取得する場合
  n = int(input())
  # 文字列 s を取得する場合
  s = input()
  # n 行の数値の配列 a を取得する場合
  a = []
  for i in range(n):
    a.append(input().replace('\n', '').split(" "))


if __name__ == '__main__':
  main()
