import sys

def main():
  # 提出用
  # input = sys.stdin.readline
  # デバッグ用（提出時に使うと遅い可能性あり）
  if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
  n = int(input())

  d = 'R'
  c = [0, 0]
  arr = [[None for i in range(n)] for j in range(n)]
  arr[int((n+1)/2)-1][int((n+1)/2)-1] = 'T'

  for i in range(1, n**2):
    arr[c[1]][c[0]] = i
    if d == 'R':
      if c[0]+1 >= n or arr[c[1]][c[0]+1] != None:
        d = 'D'
        c = [c[0], c[1]+1]
      else:
        c = [c[0]+1, c[1]]
    elif d == 'D':
      if c[1]+1 >= n or arr[c[1]+1][c[0]] != None:
        d = 'L'
        c = [c[0]-1, c[1]]
      else:
        c = [c[0], c[1]+1]
    elif d == 'L':
      if c[0]-1 < 0 or arr[c[1]][c[0]-1] != None:
        d = 'U'
        c = [c[0], c[1]-1]
      else:
        c = [c[0]-1, c[1]]
    elif d == 'U':
      if c[1]-1 < 0 or arr[c[1]-1][c[0]] != None:
        d = 'R'
        c = [c[0]+1, c[1]]
      else:
        c = [c[0], c[1]-1]

  for a in arr:
    print(' '.join(map(str, a)))
    

if __name__ == '__main__':
  main()
