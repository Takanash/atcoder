import sys

def main():
  input = sys.stdin.readline
  n, q = map(int, input().replace('\n', '').split(" "))
  s = input()
  for i in range(q):
    l, r = map(int, input().replace('\n', '').split(" "))
    str = s[l-1:r]
    num = 0
    for j in range(l, r):
      if s[j-1] == s[j]:
        num += 1
    print(num)


if __name__ == '__main__':
  main()
