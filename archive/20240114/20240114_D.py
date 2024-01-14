import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  from_left_dp = [1 for i in range(n)]
  # 左から動的計画法
  for i in range(1, n):
    if from_left_dp[i-1] < a[i]:
      from_left_dp[i] = from_left_dp[i-1] + 1
    else:
      from_left_dp[i] = a[i]
  # print(from_left_dp)
  
  from_right_dp = [1 for i in range(n)]
  # 右から動的計画法
  for i in reversed(range(n-1)):
    # print(f'a[i]: {a[i]}, from_right_dp: {from_right_dp}')
    if from_right_dp[i+1] < a[i]:
      from_right_dp[i] = from_right_dp[i+1] + 1
    else:
      from_right_dp[i] = a[i]
  # print(from_right_dp)
  
  ans = 1
  for i in range(n):
    l = from_left_dp[i]
    r = from_right_dp[i]
    print(f'l: {l}, r: {r}, ans: {ans}')
    if l >= r and r > ans:
      ans = r
    elif r >= l and l > ans:
      ans = l

  print(ans)

# 時間計測用
# import time
# start = time.time()

if __name__ == '__main__':
  main()

# end = time.time()
# time_diff = end - start
# print(f"実行時間: {str(time_diff)}")
