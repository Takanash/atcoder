import sys
import time

def main():
  input = sys.stdin.readline
  n, k = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  # sum = binary(n, k, a)
  sum = shakutori(n, k, a)
  print(sum)
    

# しゃくとり法で計算する場合
def shakutori(n, k, a):
  sum = 0
  j = 1
  for i in range(n):
    # Ri = Ri-1 (= j) からスタートする
    # i < j の場合、a[i]からa[j-1]まではa[i]との差がk以下とみなせるため、sumに j - (i + 1) を足してしまって良い
    sum += j - (i + 1) 
    while j < n and a[i] + k >= a[j]:
      # print(f"i: {i}, j: {j}, sum: {sum}")
      sum += 1
      j += 1
  return sum


# 二分探索で計算する場合
def binary(n, k, a):
  sum = 0
  for i in range(n):
    left = 0
    right = n - 1

    while left < right:
      mid = int((left + right) / 2)
      # print(f"left: {left}, right: {right}, mid: {mid}, a[i]: {a[i]}, a[mid]: {a[mid]}, sum: {sum}")
      if a[mid] > a[i] + k:
        right = mid
      else:
        left = mid + 1
    
    if a[left] > a[i] + k:
      sum += left - 1 - i
    else:
      sum += left - i
  return sum



# start = time.time()

if __name__ == '__main__':
  main()

# end = time.time()
# time_diff = end - start
# print(f"実行時間: {str(time_diff)}")
