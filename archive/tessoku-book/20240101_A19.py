import sys

def main():
  input = sys.stdin.readline
  n, w = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [list(map(int, input().replace("\n", "").split(" "))) for i in range(n)]

  partial_sum = [[-1 for i in range(w+1)] for j in range(n+1)]
  partial_sum[0][0] = 0

  for i in range(1, n+1):
    item_w = a[i-1][0]
    item_v = a[i-1][1]
    for j in range(w+1):
      if j - item_w >= 0 and partial_sum[i-1][j-item_w] >= 0:
        if partial_sum[i-1][j] <= partial_sum[i-1][j-item_w] + item_v:
          partial_sum[i][j] = partial_sum[i-1][j-item_w] + item_v
        else:
          partial_sum[i][j] = partial_sum[i-1][j]
      elif partial_sum[i-1][j] >= 0:
        partial_sum[i][j] = partial_sum[i-1][j]

  # 平坦化した動的計画法の配列の最大値が取りうる価値の最大値となる
  print(max(sum(partial_sum, [])))

if __name__ == '__main__':
  main()
