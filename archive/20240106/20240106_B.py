import sys

def main():
  input = sys.stdin.readline
  n = int(input())

  for x in range(22):
    for y in range(22):
      for z in range(22):
        if x + y + z <= n:
          print(f'{x} {y} {z}')

if __name__ == '__main__':
  main()
