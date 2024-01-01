import sys

def main():
  input = sys.stdin.readline
  n, s = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  partial_sum = [[None for i in range(s+1)] for j in range(n+1)]
  partial_sum[0][0] = True
  for i in range(1, s+1):
    partial_sum[0][i] = False

  for i in range(1, n+1):
    target_card = a[i-1]
    for j in range(s+1):
      if partial_sum[i-1][j] or (j >= target_card and partial_sum[i-1][j-target_card]):
        partial_sum[i][j] = True
      else:
        partial_sum[i][j] = False

  flg = False
  for arr in partial_sum:
    if arr[-1]:
      flg = True
  
  if flg:
    print("Yes")
  else:
    print("No")

if __name__ == '__main__':
  main()
