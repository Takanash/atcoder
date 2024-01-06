import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  x_y = [map(int, input().replace('\n', '').split(' ')) for i in range(n)]
  q = int(input())
  abcd = [map(int, input().replace('\n', '').split(' ')) for i in range(q)]

  arr = [[0 for i in range(1501)] for j in range(1501)]
  for x, y in x_y:
    arr[y][x] += 1
  
  prefix_sum = [[0 for i in range(1501)] for j in range(1501)]
  for i in range(1, 1501):
    prefix_sum[0][i] = prefix_sum[0][i-1] + arr[0][i]
  for y in range(1, 1501):
    prefix_sum[y][0] = prefix_sum[y-1][0] + arr[y][0]
    for x in range(1, 1501):
      prefix_sum[y][x] = prefix_sum[y][x-1] + prefix_sum[y-1][x] - prefix_sum[y-1][x-1] + arr[y][x]

  # for i in arr:
  #   print(i)
  # print()

  # for i in prefix_sum:
  #   print(i)

  for a, b, c, d in abcd:
    tmp = prefix_sum[d][c] - prefix_sum[d][a-1] - prefix_sum[b-1][c] + prefix_sum[b-1][a-1]
    print(tmp)


if __name__ == '__main__':
  main()
