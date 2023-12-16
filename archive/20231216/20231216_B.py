import sys

def main():
  input = sys.stdin.readline
  s = input().replace('\n', '')
  t = input().replace('\n', '')
  str = "ABCDE"
  s_diff = abs(str.find(s[0]) - str.find(s[1]))
  t_diff = abs(str.find(t[0]) - str.find(t[1]))
  if (s_diff == 1 or s_diff == 4) and (t_diff == 1 or t_diff == 4):
    print("Yes")
  elif (s_diff == 2 or s_diff == 3) and (t_diff == 2 or t_diff == 3):
    print("Yes")
  else:
    print("No")


if __name__ == '__main__':
  main()
