import sys
import time

def main():
  input = sys.stdin.readline
  a, b = [int(i) for i in input().replace('\n', '').split(' ')]
  print(str(a + b))

if __name__ == '__main__':
  main()

