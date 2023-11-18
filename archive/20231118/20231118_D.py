import sys
import time

def main():
  input = sys.stdin.readline
  n, m = [int(i) for i in input().replace('\n', '').split(" ")]
  a = [int(i) for i in input().replace('\n', '').split(" ")]

  count_arr = [0] * n
  count_arr[a[0]-1] += 1
  tmp_max = 1
  number = a[0]
  print(a[0])

  for i in a[1:]:
    count_arr[i-1] += 1
    if tmp_max < count_arr[i-1]:
      tmp_max = count_arr[i-1]
      number = i
    elif tmp_max == count_arr[i-1]:
      if i < number:
        number = i
    print(number)


if __name__ == '__main__':
  main()
