import sys

def main():
  input = sys.stdin.readline
  n, x = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  index = binary_search(a, x, 0, len(a)-1)
  print(index+1)

# 二分探索のメソッド
# start: 探索開始のインデックス
# end: 探索終了のインデックス
# index: start, endの中心のインデックス
def binary_search(arr, x, start, end):
  index = start + (end - start) // 2 
  if arr[index] < x:
    return binary_search(arr, x, index+1, end)
  elif arr[index] > x:
    return binary_search(arr, x, start, index-1)
  else:
    return index 


if __name__ == '__main__':
  main()
