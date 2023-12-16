import sys

def main():
  input = sys.stdin.readline
  n = int(input())

  sum = 0
  prev_sum = 0
  index = 0
  # 1 <= N <= 333の前提で、333の場合レピュニットは"1"*12
  # 必要な分のレピュニットの配列を生成する
  repunite = [int("1" * i) for i in range(1, 13)]

  # n番目に小さいレピュニットを生成するために何番目のレピュニットまで必要かを計算する
  # indexは1始まりなのでrepuniteのインデックスとして使う場合は-1する
  # 例えば5であれば、111まで必要なのでindex: 3となる
  while sum < n:
    index += 1
    prev_sum = sum
    sum = prev_sum + int(index * (index+1) / 2)
    # print(f"index: {index}, sum: {sum}, prev_sum: {prev_sum}")

  arr = []
  for i in range(index):
    for j in range(index):
      arr.append(repunite[i] + repunite[j] + repunite[index-1])

  # 重複を取り除いて昇順にソートする
  arr = list(set(arr))
  arr.sort()
  print(arr[n-prev_sum-1])

  # 計算量的に1つを固定した方が良いと思ったが単純な全探索でも計算時間が余裕だった
  # （よく考えたら計算量が12^3なのでそりゃそう）
  # 以下は回答後に考えた答え
  # arr = []
  # for i in range(12):
  #   for j in range(12):
  #     for k in range(12):
  #       print(f"i: {i}, j: {j}, k: {k}")
  #       arr.append(repunite[i] + repunite[j] + repunite[k])
  # arr = list(set(arr))
  # arr.sort()
  # print(arr[n-1])



if __name__ == '__main__':
  main()
