import sys
import time

def main():
  input = sys.stdin.readline
  str_arr = list(input().replace("\n", ""))
  print(" ".join(str_arr))


if __name__ == '__main__':
  main()
