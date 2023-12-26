import sys

def main():
  input = sys.stdin.readline
  n, k = [int(i) for i in input().replace('\n', '').split(' ')]
  a = [int(i) for i in input().replace('\n', '').split(' ')]

  left = 1
  right = 10 ** 9

  while left < right:
    mid = int((left + right) / 2)
    if check(mid, a, k):
      right = mid
    else:
      left = mid + 1
  print(left)

  
def check(seconds, a, k):
  print_sum = sum([int(seconds / i) for i in a])
  if print_sum >= k:
    return True
  else:
    return False


# 以下
# def main():
#   input = sys.stdin.readline
#   n, k = [int(i) for i in input().replace('\n', '').split(' ')]
#   a = [int(i) for i in input().replace('\n', '').split(' ')]

#   seconds = get_print_time(a, k)
#   print(seconds)


# def get_print_time(arr, target_sheets_num):
#   start = 1
#   end = 1000000000

#   while(True):
#     # start, endの真ん中の秒数を算出
#     seconds = (start + end) // 2
#     # secondsでの印刷枚数を算出
#     sheets_num = 0
#     for sheets_per_second in arr:
#       sheets_num += seconds // sheets_per_second
    
#     # print(f"start: {start}")
#     # print(f"end: {end}")
#     # print(f"seconds: {seconds}")
#     # print(f"sheets_num: {sheets_num}\n")
#     # sleep(2)

#     if start >= end:
#       # start == endの場合は探索終了とし、k枚印刷される最小の秒数を返す
#       if sheets_num < target_sheets_num:
#         return seconds + 1
#       else:
#         return seconds
#     elif target_sheets_num < sheets_num:
#       end = seconds - 1
#     elif sheets_num < target_sheets_num:
#       start = seconds + 1
#     else: # sheets_num == target_sheets_num
#       return seconds
    

if __name__ == '__main__':
  main()
