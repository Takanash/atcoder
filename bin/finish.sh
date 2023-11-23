#!/bin/bash

dir=`date +'%Y%m%d'`

if [ $# = 1 ]; then
  dir=$1
fi

filecount=`find . -maxdepth 1 -type f -name '*.py' | wc -l`
if [ $filecount -ge 1 ]; then
  eval "mkdir -p archive/$dir"
  eval "mv *.py archive/$dir"
else
  echo "対象のファイルがないためアーカイブされませんでした"
fi
