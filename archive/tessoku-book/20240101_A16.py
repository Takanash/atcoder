import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  a = [int(i) for i in input().replace('\n', '').split(' ')]
  b = [int(i) for i in input().replace('\n', '').split(' ')]

  # 部屋1→1を移動する所要時間は0のため、あらかじめ0を配列に入れる
  times = [0]
  for i in range(n-1):
    # print(times)
    if i == 0:
      # iが0のとき（=部屋1→2への移動）
      move_one = a[i]
      times.append(move_one)
    else:
      # i=3の場合、部屋1→2+部屋2→4への移動の所要時間
      move_two = times[-2] + b[i-1]
      # i=3の場合、部屋1→3+部屋3→4への移動の所要時間
      move_one = times[-1] + a[i]
      # 小さい方の所要時間を最短の所要時間とする
      if move_one >= move_two:
        times.append(move_two)
      else:
        times.append(move_one)
  
  print(times[-1])

if __name__ == '__main__':
  main()
