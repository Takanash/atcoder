import sys

def main():
  input = sys.stdin.readline
  n, q = [int(i) for i in input().replace('\n', '').split(" ")]
  a = [int(i) for i in input().replace('\n', '').split(" ")]
  # L1~LQ, R1~RQの標準出力をintに変換した上で二重配列に入れる
  # l_r_arr = [[2, 3], [1, 4], ...]
  l_r_arr = [[int(j) for j in input().replace('\n', '').split(" ")] for i in range(q)]
  cumulative_sum = [0]

  # 来場者数の累積和を出す
  for num in a:
    cumulative_sum.append(cumulative_sum[-1] + num)

  # cumulative_sum[0]は0日目と考えると、2日目から3日目の合計来場者数は
  # cumulative_sum[l(=3)] - cumulative_sum[r-1(=1)]となる
  for l_r in l_r_arr:
    l, r = l_r
    print(cumulative_sum[r] - cumulative_sum[l-1])


if __name__ == '__main__':
  main()
