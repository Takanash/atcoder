import sys
import time

def main():
  input = sys.stdin.readline
  n = int(input())
  s = input().replace("\n", "")
  char_count = {s[0]: 1}
  tmp_char = s[0]
  tmp_num = 1
  for c in s[1:]:
    if tmp_char == c:
      tmp_num += 1
    else:
      if char_count[tmp_char] < tmp_num:
        char_count[tmp_char] = tmp_num
      tmp_num = 1
      tmp_char = c
      if not char_count.get(c):
        char_count[c] = 1
  if char_count[tmp_char] < tmp_num:
    char_count[tmp_char] = tmp_num
  
  sum = 0
  for n in char_count.values():
    sum += n
  print(sum)  
      

if __name__ == '__main__':
  main()
