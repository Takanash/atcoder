import sys
import bisect

# sample_01.txt のみRE
# AtCoderのコードテストで実行してもエラーが発生しないため原因不明
def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  sort_a = list(set(a.copy()))
  sort_a.sort()

  arr = []
  for i in range(n):
    index = bisect.bisect_left(sort_a, a[i])
    arr.append(str(index + 1))

  print(*arr)
  

if __name__ == '__main__':
  main()
