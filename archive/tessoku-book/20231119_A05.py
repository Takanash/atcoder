import sys

def main():
  input = sys.stdin.readline
  n, k = [int(i) for i in input().replace('\n', '').split(" ")]
  count = 0
  for x in range(1, n+1):
    for y in range(1, n+1):
      z = k - (x + y)
      if 1 <= z and z <= n:
        count += 1
  print(count)


if __name__ == '__main__':
  main()
