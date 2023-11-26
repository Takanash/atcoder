import sys

def main():
  input = sys.stdin.readline
  n, l, r = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  ans = []
  for n in a:
    if n <= l:
      ans.append(l)
    elif l < n and n < r:
      ans.append(n)
    else:
      ans.append(r)
  print(' '.join(map(str, ans)))


if __name__ == '__main__':
  main()
