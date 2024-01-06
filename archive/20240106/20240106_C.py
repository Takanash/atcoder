import sys

def main():
  input = sys.stdin.readline
  n, q = [int(i) for i in input().replace('\n', '').split(' ')]

  arr = []
  for i in reversed(range(n)):
    arr.append([i+1, 0])

  for i in range(q):
    query, x = input().replace('\n', '').split(' ')
    if query == '1':
      if x == 'R':
        arr.append([arr[-1][0]+1, arr[-1][1]])
      elif x == 'L':
        arr.append([arr[-1][0]-1, arr[-1][1]])
      elif x == 'U':
        arr.append([arr[-1][0], arr[-1][1]+1])
      elif x == 'D':
        arr.append([arr[-1][0], arr[-1][1]-1])
    elif query == '2':
      c = arr[-int(x)]
      print(f'{c[0]} {c[1]}')

if __name__ == '__main__':
  main()
