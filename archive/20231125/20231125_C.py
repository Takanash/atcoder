import sys
import bisect

# 以下を参考に回答作成
# https://atcoder.jp/contests/abc330/submissions/47954237
def main():
  input = sys.stdin.readline
  d = int(input())

  x_arr = []
  for x in range(int(2e6+10)):
    x_arr.append(x**2)
  
  ans = float('inf')
  # yの値を二分探索で探す
  for x_squared in x_arr:
    z = x_squared - d
    y_index = bisect.bisect_left(x_arr, -z)
    if y_index == len(x_arr):
      # y > x_arr[-1] の場合
      # x_arr の範囲を取りうるDの範囲より大きくしているため、通常ここに入ることはない
      ans = min(ans, abs(z + x_arr[-1]))
    elif y_index == 0:
      # yが0の場合
      # x_squared > d のため、 y は必ず1となる
      ans = min(ans, abs(z + x_arr[0]))
    else:
      # 0 < y < x_arr[-1]の場合
      # y = x_arr[y_index], y = x_arr[y_index-1] の2パターンの最小を比較する
      ans = min(ans, abs(z + x_arr[y_index]), abs(z + x_arr[y_index-1]))
  print(ans)


if __name__ == '__main__':
  main()
