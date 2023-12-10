import sys

def main():
  input = sys.stdin.readline
  n, s, k = [int(i) for i in input().replace('\n', '').split(' ')]
  p_q = [input().replace('\n', '').split(' ') for i in range(n)]

  sum = 0
  for p, q in p_q:
    sum += int(p) * int(q)
  
  if sum >= s:
    print(sum)
  else:
    print(sum + k)
  

if __name__ == '__main__':
  main()
