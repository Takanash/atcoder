import sys

def main():
  input = sys.stdin.readline
  s = input().replace('\n', '')
  t = input().replace('\n', '')
  len_s = len(s)
  len_t = len(t)

  partial_sum = [[0 for i in range(len_t+1)] for j in range(len_s+1)]

  for i in range(len_s+1):
    for j in range(len_t+1):
      # print(f"i: {i}, j: {j}, s[i-1]: {s[i-1]}, t[i-1]: {t[j-1]}")
      if i >= 1 and j >= 1 and s[i-1] == t[j-1]:
        partial_sum[i][j] = max(partial_sum[i-1][j], partial_sum[i][j-1], partial_sum[i-1][j-1]+1)
      elif i >= 1 and j >= 1:
        partial_sum[i][j] = max(partial_sum[i-1][j], partial_sum[i][j-1])
      elif i >= 1:
        partial_sum[i][j] = partial_sum[i-1][j]
      elif j >= 1:
        partial_sum[i][j] = partial_sum[i][j-1]
  print(partial_sum[len_s][len_t])


if __name__ == '__main__':
  main()
