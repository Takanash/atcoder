#!/bin/bash

if [ $# -ne 1 ]; then
  dir=$1
else
  dir=`date +'%Y%m%d'`
fi

filecount=`find . -maxdepth 1 -type f -name *.py | wc -l`

if [ $filecount -ge 1 ]; then
  eval "mkdir archive/$dir"
  eval "mv *.py archive/$dir" 
else
  echo "対象のファイルがないためアーカイブされませんでした"
fi
