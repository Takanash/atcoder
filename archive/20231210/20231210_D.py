import sys
import time

# WA
def main():
  input = sys.stdin.readline
  h, w = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [[int(i) for i in input().replace('\n', '').split(' ')] for j in range(h)]
  b = [[int(i) for i in input().replace('\n', '').split(' ')] for j in range(h)]

  is_match = True

  for i in range(h):
    # aのi行目
    h_a = a[i]
    flg = False
    for j in range(h):
      # bのi行目
      h_b = b[j]
      for k, num_a in enumerate(h_a):
        # aのHi行目のそれぞれの文字がbのi行目に存在するかを確認する
        if not num_a in h_b:
          break
        if k+1 == len(h_a):
          flg = True
    if not flg:
      is_match = False
  
  print(is_match)


# start = time.time()

if __name__ == '__main__':
  main()

# end = time.time()
# time_diff = end - start
# print(f"実行時間: {str(time_diff)}")
