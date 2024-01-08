import sys
import itertools

def main():
  input = sys.stdin.readline
  n = int(input())

  x_max = 0
  y_max = 0

  abcd = []
  for i in range(n):
    a, b, c, d = list(map(int, input().replace('\n', '').split(' ')))
    abcd.append([a, b, c, d])
    if c > x_max:
      x_max = c
    if d > y_max:
      y_max = d

  arr = [[0 for i in range(x_max+1)] for j in range(y_max+1)]
  prefix_sum = [[0 for i in range(x_max+1)] for j in range(y_max+1)]

  for a, b, c, d in abcd:
    arr[b][a] += 1
    arr[d][a] -= 1
    arr[b][c] -= 1
    arr[d][c] += 1
  
  # x軸方向の累積和
  for y in range(y_max+1):
    prefix_sum[y][0] = arr[y][0]
    for x in range(1, x_max+1):
      prefix_sum[y][x] = prefix_sum[y][x-1] + arr[y][x]
  
  # y軸方向の累積和
  for x in range(x_max+1):
    for y in range(1, y_max+1):
      prefix_sum[y][x] += prefix_sum[y-1][x]
  
  # print(prefix_sum)

  flatten_prefix_sum = itertools.chain.from_iterable(prefix_sum)
  total_area = (x_max+1) * (y_max+1)

  # 1以上の部分（紙が置かれている部分）を抽出した配列の配列長=面積となる
  print(total_area - len(list(filter(lambda x: x == 0, flatten_prefix_sum))))

if __name__ == '__main__':
  main()
