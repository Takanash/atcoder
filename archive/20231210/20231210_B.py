import sys

def main():
  input = sys.stdin.readline
  k, g, m = [int(i) for i in input().replace('\n', '').split(' ')]

  tmp_g = 0
  tmp_m = 0
  for i in range(k):
    # print(f"tmp_g: {tmp_g}, tmp_m: {tmp_m}")
    if tmp_g == g:
      tmp_g = 0
    elif tmp_m == 0:
      tmp_m = m
    else:
      if (g - tmp_g) >= tmp_m:
        tmp_g = tmp_m
        tmp_m = 0
      else:
        tmp_m -= g - tmp_g
        tmp_g = g
  print(f"{tmp_g} {tmp_m}")


if __name__ == '__main__':
  main()
