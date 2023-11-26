import sys

def main():
  input = sys.stdin.readline
  n, l = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]
  count = 0
  for point in a:
    if point >= l:
      count += 1
  print(count)


if __name__ == '__main__':
  main()
