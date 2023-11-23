import sys

def main():
  input = sys.stdin.readline
  h, w = [int(i) for i in input().replace('\n', '').split(' ')]
  table = [[int(i) for i in input().replace('\n', '').split(' ')] for j in range(h)]

  # NOTE: 以下のコードでは配列の生成と計算を一気にやろうとしているが、
  #       (h+1)*(w+1)の0埋め配列を作る → 横方向の累積和を計算 → 縦方向の累積和を計算
  #       の方が多少コードは増えるが分かりやすいと思われる
  sum_table = [[0 for i in range(w+1)]]
  for y in range(h):
    tmp_arr = [0]

    for x in range(w):
      sum = tmp_arr[-1] + table[y][x] + sum_table[y][x+1] - sum_table[y][x]
      tmp_arr.append(sum)
    sum_table.append(tmp_arr)
  q = int(input())

  for i in range(q):
    a, b, c, d = [int(i) for i in input().replace('\n', '').split(' ')]
    sum = sum_table[c][d] - sum_table[c][b-1] - sum_table[a-1][d] + sum_table[a-1][b-1]
    print(sum)

if __name__ == '__main__':
  main()
