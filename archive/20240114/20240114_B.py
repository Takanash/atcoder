import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  b = format(n, 'b')

  count = 0
  for c in reversed(list(b)):
    if c == '0':
      count += 1
    else:
      break

  print(count)


if __name__ == '__main__':
  main()
