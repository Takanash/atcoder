import sys

DEBUG=False
TIME=False

def main():
  s = input()
  
  if len(s) > 0:
    tmp_c = s[0]
  is_abc = True

  for c in s[1:]:
    # print(f'c: {c}, tmp_c: {tmp_c}')
    if c == 'A':
      if tmp_c != 'A':
        is_abc = False
        break
    if c == 'B':
      if not (tmp_c == 'A' or tmp_c == 'B'):
        is_abc = False
        break
    tmp_c = c
  
  if is_abc:
    print('Yes')
  else:
    print('No')



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


# 10進数→n進数への変換
# @param [int] value 変換する値
# @param [int] base 変換するn進数
# @return [str] n進数に変換した値
def base10int(value, base):
    if (int(value / base)):
        return base10int(int(value / base), base) + str(value % base)
    return str(value % base)
