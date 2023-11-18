import sys
import time

def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(" ")]
  max_num = max(a)
  arr = [i for i in a if i != max_num]
  print(max(arr))


if __name__ == '__main__':
  main()
