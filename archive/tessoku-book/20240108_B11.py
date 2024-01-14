import sys
import bisect

def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(' ')]
  q = int(input())
  x = [int(input()) for i in range(q)]

  a.sort()

  for x_i in x:
    tmp = bisect.bisect_left(a, x_i)
    print(tmp)


if __name__ == '__main__':
  main()
