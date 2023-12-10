import sys

def main():
  input = sys.stdin.readline
  n, m = [int(i) for i in input().replace('\n', '').split(' ')]
  s = input().replace('\n', '')

  # 最小のTシャツの枚数
  answer = 0

  for x in range(1001):
    # print(f"--- x: {x} ---")
    answer = x
    # tmp_x: i日目でのロゴ入りTシャツの枚数
    # tmp_m: i日目での無地Tシャツの枚数
    tmp_x = x
    tmp_m = m
    flg = True
    for c in s:
      if c == "0":
        tmp_x = x
        tmp_m = m
      elif c == "1":
        if tmp_m > 0:
          tmp_m -= 1
        else:
          tmp_x -= 1
      else:
        tmp_x -= 1

      # print(f"tmp_x: {tmp_x}, tmp_m: {tmp_m}")
      
      if tmp_x < 0:
        flg = False
        break
    if flg:
      break
  
  print(answer)


if __name__ == '__main__':
  main()
