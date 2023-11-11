import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  d = map(int, input().replace('\n', '').split(" "))
  same_numbers = 0

  for i, days in enumerate(d):
    month = i + 1
    for day in range(1, days+1):
      date = str(month) + str(day)
      if len(set(date)) == 1:
        same_numbers += 1

  print(same_numbers)


if __name__ == '__main__':
  main()
