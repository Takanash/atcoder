import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  for i in range(n):
    for j in range(n):
      if i == j:
        break
      for k in range(n):
        if i == k or j == k:
          break
        if a[i] + a[j] + a[k] == 1000:
          print("Yes")
          return
  print("No")


if __name__ == '__main__':
  main()
