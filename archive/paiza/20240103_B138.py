import sys

def main():
  input = sys.stdin.readline
  h, w = [int(i) for i in input().replace('\n', '').split(' ')]
  s = [list(input().replace('\n', '')) for i in range(h)]

  count = 0
  for y in range(h-2):
    for x in range(w-2):
      # ドーナツの左上を(x, y)とする
      if not (s[y][x]     == '#' and
              s[y][x+1]   == '#' and
              s[y][x+2]   == '#' and
              s[y+1][x]   == '#' and
              s[y+1][x+1] == "." and
              s[y+1][x+2] == '#' and 
              s[y+2][x]   == '#' and
              s[y+2][x+1] == '#' and
              s[y+2][x+2] == '#'
              ):
        continue
      count += 1
  
  print(count)
      

if __name__ == '__main__':
  main()
