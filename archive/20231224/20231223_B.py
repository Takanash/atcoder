import sys

# WA
def main():
  input = sys.stdin.readline
  a, m, l, r = [int(i) for i in input().replace('\n', '').split(' ')]

  # 起点を0として考えるために、l, rからaを引く
  l_a = l - a # -6
  r_a = r - a # 1

  sum = 0
  if l_a >= 0 and r_a >= 0:
    sum += int(r_a / m) - int(l_a / m)
    if l_a % m == 0:
      sum += 1
  elif l_a <= 0 and r_a <= 0:
    sum += abs(int(l_a / m)) - abs(int(r_a / m))
    if r_a % m == 0:
      sum += 1
  else:
    sum += abs(int(l_a / m)) + int(r_a / m)
    sum += 1

  print(sum)

if __name__ == '__main__':
  main()
