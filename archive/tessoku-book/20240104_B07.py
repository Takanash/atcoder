import sys
import time

def main():
  if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
  t = int(input())
  n = int(input())
  l_r = [map(int, input().replace('\n', '').split(' ')) for i in range(n)]

  prefix_sum = [0 for i in range(t+1)]

  for l, r in l_r:
    prefix_sum[l] += 1
    prefix_sum[r] -= 1
  
  tmp = 0
  for n in prefix_sum[:-1]:
    tmp += n
    print(tmp)

if __name__ == '__main__':
  main()
