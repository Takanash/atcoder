AtCoder用スクリプト（Python3/pypy）

# 前提
pyenvが導入されていること
```
❯ pyenv versions
  system
  3.11.6
* pypy3.10-7.3.12
```

# ディレクトリ
```
.
├── README.md
├── archive         # 過去の回答
├── bin
│   ├── finish.sh   # コンテスト終了時にアーカイブするスクリプト
│   └── start.sh    # 問題に着手する際にファイル（ファイル名は`[今日の日付]_[問題番号].py`）を作成するスクリプト
├── input.txt       # 標準入力
└── template
    └── template.py # python3用テンプレート
```

# 使い方
## 開始
```
./bin/start.sh [問題番号]
ex)
./bin/start.sh A
=> ./[今日の日付]_A.py が作成される
```

## テスト
```
python [ファイル名].py < input.txt
```

## 終了
```
./bin/finish.sh
=> ./*.py のファイルが ./archive/[今日の日付] 内に移動される

./bin/finish.sh 20230101
=> ./*.py のファイルが ./archive/20230101 内に移動される
```
