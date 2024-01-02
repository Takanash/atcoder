import sys

def main():
  input = sys.stdin.readline
  a, b = [int(i) for i in input().replace('\n', '').split(' ')]
  for i in range(a, b+1):
    if 100 % i == 0:
      print("Yes")
      return
  print("No")

if __name__ == '__main__':
  main()
