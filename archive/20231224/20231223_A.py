import sys

def main():
  input = sys.stdin.readline
  b, g = [int(i) for i in input().replace('\n', '').split(' ')]
  if b > g:
    print("Bat")
  else:
    print("Glove")


if __name__ == '__main__':
  main()
