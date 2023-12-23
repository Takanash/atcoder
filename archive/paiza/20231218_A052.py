import sys
import time

def main():
  input = sys.stdin.readline
  n = int(input())
  a, b = [int(i) for i in input().replace('\n', '').split(' ')]

  # 踏む段をarrに追加していく
  # 最後の段は必ず踏むため最初からnを入れる
  arr = [n]
  y = 0
  for i in range(1, n):
    y = 0
    # 式を ax + by = i とし、変形すると x = (i - by) / a
    # (i - by) % a == 0（＝xが整数）かつ(i - by) >= 0の場合は踏む段とみなせる
    while y * b <= i:
      tmp = i - b * y
      # print(f"y: {y}, i: {i}, tmp: {tmp}")
      if tmp % a == 0 and tmp >= 0:
        arr.append(i)
        break
      y += 1
  # print(set(arr))
  # n から踏む段の数を引いた数が踏まない段の数
  print(n - len(set(arr)))


start = time.time()

if __name__ == '__main__':
  main()

end = time.time()
time_diff = end - start
print(f"実行時間: {str(time_diff)}")
