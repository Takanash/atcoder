import sys
import math

def main():
  input = sys.stdin.readline
  a = []
  is_yes = "Yes"
  for i in range(9):
    a.append(input().replace('\n', '').split(" "))
  # 横の列のチェック
  for i in range(9): # 縦のインデックス
    tmp = []
    for j in range(9):
      if a[i][j] in tmp: # 横のインデックス
        is_yes = "No"
        break
      tmp.append(a[i][j])
    if is_yes == "No":
      break
  # 縦の列のチェック
  for i in range(9): # 縦のインデックス
    tmp = []
    for j in range(9): # 横のインデックス
      if a[j][i] in tmp:
        is_yes = "No"
        break
      tmp.append(a[j][i])
    if is_yes == "No":
      break
  # 3 × 3のマス目の存在チェック
  for i in range(3): # 縦の3 × 3の範囲
    for j in range(3): # 横の3 × 3の範囲
      tmp = []
      for k in range(3): # 縦のインデックス
        for l in range(3): # 横のインデックス
          if a[k+(i*3)][l+(j*3)] in tmp:
            is_yes = "No"
            break
          tmp.append(a[k+(i*3)][l+(j*3)])
        if is_yes == "No":
          break
      if is_yes == "No":
        break
    if is_yes == "No":
      break

  print(is_yes)


if __name__ == '__main__':
  main()
