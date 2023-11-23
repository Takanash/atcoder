#!/bin/bash

if [ $# -ne 1 ]; then
  echo "ABCの問題番号を指定して下さい ex) bin/start.sh A" 1>&2
  exit 1
fi

touch input.txt

filename=`date +"%Y%m%d"`_$1.py
if [ -e $filename ]; then
  echo "ファイルが既に存在するためファイルの作成をスキップします"
else
  eval "cp template/template.py `date +"%Y%m%d"`_$1.py"
fi
