import sys

def main():
  n = int(input())

  r = 100000
  l = 1
  mid = (l + r) / 2

  while(l <= r):
    mid = (l + r) / 2
    tmp = mid ** 3 + mid
    if tmp == n:
      break
    elif tmp > n:
      r = mid - 0.0001
    else:
      l = mid + 0.0001

  print(mid)
  
    
if __name__ == '__main__':
  main()
