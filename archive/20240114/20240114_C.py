import sys

def main():
  # 提出用
  # input = sys.stdin.readline
  # デバッグ用（提出時に使うと遅い可能性あり）
  if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
  
  # n番目なのであらかじめ1を引く
  n = int(input()) - 1
  pen_n = int(base10int(n, 5))
  a = [0, 2, 4, 6, 8]

  ans = 0
  for i, x in enumerate(reversed((str(pen_n)))):
    ans += a[int(x)] * 10 ** i

  print(ans)

# 10進数→n進数への変換
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)


if __name__ == '__main__':
  main()
