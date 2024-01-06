import sys
import itertools

# WA
def main():
  # 提出用
  # input = sys.stdin.readline
  # デバッグ用（提出時に使うと遅い可能性あり）
  if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
  n, m = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]
  u_v = [list(map(int, input().replace('\n', '').split(' '))) for i in range(n)]

  d = {}
  for i, a_i in enumerate(a, 1):
    d[i] = [a_i]
  # t = sorted(d.items(), key=lambda x:x[1])
  # d2 = {k:v for k, v in t}

  sorted_u_v = sorted(u_v)

  arr = [[] for i in range(n)]

  for u, v in sorted_u_v:
    if d[v][0] >= d[u][0]:
      d[v] += d[u] + d[v]
  print(d)
  print(len(set(d[n][1:])))


# 時間計測用
# import time
# start = time.time()

if __name__ == '__main__':
  main()

# end = time.time()
# time_diff = end - start
# print(f"実行時間: {str(time_diff)}")
