import sys

def main():
  input = sys.stdin.readline
  n = input()
  print((n * int(n)).replace("\n", ""))


if __name__ == '__main__':
  main()
