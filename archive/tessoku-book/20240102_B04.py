import sys

def main():
  input = sys.stdin.readline
  n = input().replace('\n', '')

  count = 0
  sum = 0
  for c in reversed(n):
    if int(c) == 1:
      sum += 2 ** count
    count += 1
  print(sum)


if __name__ == '__main__':
  main()
