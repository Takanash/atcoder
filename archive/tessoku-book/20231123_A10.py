import sys
from collections import deque

def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(' ')]
  d = int(input())

  # 左（1号室）から見た部屋数の最大値の配列を作る
  max_arr_from_left = []
  tmp_max = 0
  for i in range(n):
    if a[i] > tmp_max:
      max_arr_from_left.append(a[i])
      tmp_max = a[i]
    else:
      max_arr_from_left.append(tmp_max)
 
  # 右（n号室）から見た部屋数の最大値の配列を作る
  max_arr_from_right = deque([])
  tmp_max = 0
  for i in range(1, n+1):
    if a[-i] > tmp_max:
      max_arr_from_right.appendleft(a[-i])
      tmp_max = a[-i]
    else:
      max_arr_from_right.appendleft(tmp_max)

  for i in range(d):
    l, r = [int(j) for j in input().replace('\n', '').split(' ')]
    # l日目から工事が始まるので、配列のインデックス(l-1)の1日前（l-2）が左から見た際の最大値となる
    left_max = max_arr_from_left[l-2]
    # r日目に工事が終わるので、配列のインデックス(r-1)の1日後（r）が右から見た際の最大値となる
    right_max = max_arr_from_right[r]
    if left_max >= right_max:
      print(left_max)
    else:
      print(right_max)

if __name__ == '__main__':
  main()
