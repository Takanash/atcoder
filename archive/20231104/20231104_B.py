import sys
import math

def main():
  input = sys.stdin.readline
  b = int(input())
  # x^x <= 10^18 を満たす最大のxが15のため16を指定
  n = 16
  num = -1
  for i in range(1, n):
    if i**i == b:
      num = i
      break
  print(num)


if __name__ == '__main__':
  main()
