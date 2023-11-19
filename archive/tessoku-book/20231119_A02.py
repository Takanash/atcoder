import sys
import time

def main():
  input = sys.stdin.readline
  n, x = [int(i) for i in input().replace('\n', '').split(" ")]
  a = [int(i) for i in input().replace('\n', '').split(" ")]
  is_exist = "No"
  for num in a:
    if num == x:
      is_exist = "Yes"
      break
  print(is_exist)

if __name__ == '__main__':
  main()
