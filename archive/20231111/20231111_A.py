import sys

def main():
  input = sys.stdin.readline
  n, x = map(int, input().replace('\n', '').split(" "))

  s = map(int, input().replace('\n', '').split(" "))

  sum = 0
  for point in s:
    if point <= int(x):
      sum += point
  print(sum)


if __name__ == '__main__':
  main()
