import sys

# WA
def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(' ')]
  p = [int(i) for i in input().replace('\n', '').split(' ')]

  sum = 0
  for i in range(1, n):
    if p[i-1] != 1:
      continue
    print(a[i])
    sum += a[i]

  a0 = a[0] + sum * pow(10, 100)

  if a0 == 0:
    print("0")
  elif a0 < 0:
    print("-")
  else:
    print("+")




if __name__ == '__main__':
  main()
