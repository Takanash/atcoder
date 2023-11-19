import sys

def main():
  input = sys.stdin.readline
  d = int(input())
  n = int(input())
  l_r_arr = [[int(j) for j in input().replace("\n", "").split(" ")] for i in range(n)]
  # 8日の場合、8日目に1人入場者が減ると9日目に-1が加算されることになるため、
  # d+1しないとエラーになる
  cumulative_sum = [0 for i in range(d+1)]

  for l_r in l_r_arr:
    l, r = l_r
    cumulative_sum[l-1] += 1
    cumulative_sum[r] -= 1

  count = 0
  # 9日目は出力しないためcumulative_sum[:-1]とする
  for fluctuation in cumulative_sum[:-1]:
    count += fluctuation
    print(count)


if __name__ == '__main__':
  main()
