import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(' ')]
  q = int(input())
  l_r = [map(int, input().replace('\n', '').split(' ')) for i in range(q)]

  prefix_sum = [0 for i in range(n+1)]

  for i, kuji in enumerate(a):
    if kuji == 1:
      prefix_sum[i+1] = prefix_sum[i] + 1
    else:
      prefix_sum[i+1] = prefix_sum[i] - 1
  
  for l, r in l_r:
    num = prefix_sum[r] - prefix_sum[l-1]
    if num > 0:
      print('win')
    elif num == 0:
      print('draw')
    else:
      print('lose')

if __name__ == '__main__':
  main()
