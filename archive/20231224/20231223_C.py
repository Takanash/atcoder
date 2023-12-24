import sys
import time

# WA, RE
def main():
  input = sys.stdin.readline
  n, k = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  arr = [2 for i in range(n)]

  for i in a:
    arr[i-1] -= 1
  
  tmp = -1
  arr2 = []
  for i, x in enumerate(arr):
    if x == 1:
      if tmp != -1:
        arr2.append(i - tmp)
      tmp = i

  if len(arr2) == 0:
    print(0)
  elif len(arr2) == 1:
    print(arr2[0])
  elif len(arr2) == 2:
    tmp = 0
    for i in range(len(arr2)):
      if arr2[i] > tmp:
        tmp = i
    arr2.pop(tmp)
    print(sum(arr2))
  else:
    tmp = 0
    for i in range(len(arr2)):
      if arr2[i] > tmp:
        tmp = i
    if arr2[tmp-1] >= arr2[tmp+1]:
      arr2.pop(tmp)
      arr2.pop(tmp-1)
    else:
      arr2.pop(tmp)
      arr2.pop(tmp+1)
    print(sum(arr2))

# start = time.time()

if __name__ == '__main__':
  main()

# end = time.time()
# time_diff = end - start
# print(f"実行時間: {str(time_diff)}")
