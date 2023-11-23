import sys

def main():
  input = sys.stdin.readline
  h, w, n = [int(i) for i in input().replace('\n', '').split(' ')]

  area_add_and_sub = [[0 for x in range(w+1)] for y in range(h+1)]

  # 積雪量の加算・減算を area_add_and_sub に代入する
  for i in range(n):
    a, b, c, d = [int(i) for i in input().replace('\n', '').split(' ')]
    area_add_and_sub[a-1][b-1] += 1
    area_add_and_sub[a-1][d] -= 1
    area_add_and_sub[c][b-1] -= 1
    area_add_and_sub[c][d] += 1

  snowfall_area = []

  # area_add_and_sub から横方向のみの積雪量を snowfall_area に代入する
  for y in range(h):
    tmp_arr = []
    tmp_x = 0
    for x in range(w):
      tmp_x += area_add_and_sub[y][x]
      tmp_arr.append(tmp_x)
    snowfall_area.append(tmp_arr)

  # area_add_and_sub から縦方向も考慮した積雪量を snowfall_area に代入する
  for y in range(1, h):
    for x in range(w):
      snowfall_area[y][x] += snowfall_area[y-1][x]
  
  # 出力
  for w_snowfall in snowfall_area:
    print(" ".join([str(i) for i in w_snowfall]))
      

if __name__ == '__main__':
  main()
