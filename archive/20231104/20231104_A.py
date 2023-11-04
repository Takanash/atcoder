import sys

def main():
  input = sys.stdin.readline
  n = int(input())
  s = input()
  is_yes = False
  for i in range(n-1):
    if (s[i] == "a" and s[i+1] == "b") or (s[i] == "b" and s[i+1] == "a"):
      is_yes = True
      break
  if is_yes:
    print("Yes")
  else:
    print("No")  


if __name__ == '__main__':
  main()
