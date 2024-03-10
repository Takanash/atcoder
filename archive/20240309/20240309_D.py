import sys

DEBUG=True
TIME=False

def main():
  T = input()
  N = int(input())

  dp = [[float('inf') for i in range(len(T)+1)] for j in range(N+1)]
  dp[0][0] = 0

  # Aのループ
  for i in range(N):
    A_S = [int(i) if i == 0 else x for i, x in enumerate(input().split(' '))]
    A = A_S[0]
    S = A_S[1:]

    for j in range(len(T)+1):
      dp[i+1][j] = dp[i][j]

    # S(i,1)..S(i,AN)のループ
    for s in S:
      sl = len(s)

      # S(i,Ai)とTの一部が一致するか検証
      for j in range(len(T)-sl+1):
        ok = True
        # TとS(i, AN)
        for k in range(sl):
          if T[j+k] != s[k]:
            ok = False
            break

        if ok:
          dp[i+1][j+sl]=min(dp[i+1][j+sl], dp[i][j]+1)
    error(dp)

  print(dp[N][len(T)] if dp[N][len(T)] != float('inf') else -1)




# 標準エラー出力に引数を出力する
# デバッグ用
def error(*args, end="\n"):
  print(*args, end=end, file=sys.stderr)


# 10進数→n進数への変換
# @param [int] value 変換する値
# @param [int] base 変換するn進数
# @return [str] n進数に変換した値
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


# ビット全探索
# 引数の配列の数値の和であり得る組み合わせ全てを返す
# @param [list] arr 数値の配列
# @return [list] あり得る組み合わせの配列
def bitwise_binary_search(arr):
  sum_list = []
  for i in range(2 ** len(arr)):
    sum = 0 # 現在の合計値
    for j in range(len(arr)):
      wari = (2 ** j)
      if (i // wari) % 2 == 1:
        sum += arr[j]
    sum_list.append(sum)
  return sum_list


# ユークリッドの互除法
# 2つの数値の最大公約数を求める
# math.gcd(a, b) でもよい
# @param [int] a 数値
# @param [int] b 数値
# @return [int] 最大公約数
def gcd(a, b):
  while b:
    a, b = b, a % b
  return a

# 2つの数値の最小公倍数を求める
# math.lcm(a, b) でもよい
# @param [int] a 数値
# @param [int] b 数値
# @return [int] 最小公倍数
def lcm(a, b):
  return a * b // gcd(a, b)


if TIME:
  import time
  start = time.time()

if DEBUG:
  if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
else:
  input = sys.stdin.readline


if __name__ == '__main__':
  main()

if TIME:
  end = time.time()
  time_diff = end - start
  print(f"実行時間: {str(time_diff)}")
