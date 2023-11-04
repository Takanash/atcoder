AtCoder用スクリプト（Python3）

# 使い方
## 開始
```
sh bin/start.sh [問題番号]
ex)
sh bin/start.sh A
=> ./[今日の日付]_A.py が作成される
```

## テスト
```
python3 [ファイル名].py < input.txt
```

## 終了
```
sh bin/finish.sh
=> ./*.py のファイルが ./archive/[今日の日付] 内に移動される
```

# TODO
- パッケージ管理が入っていない（homebrew の python@3.11 を使っている）ので、パッケージ管理を導入してpypyで実行可能にする
