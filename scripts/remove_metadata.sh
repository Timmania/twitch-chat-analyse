#!/bin/bash
DIR=$1
OUT_DIR="$DIR/out_$DIR"

mkdir $OUT_DIR

for f in $1/*.txt
do
	cut -d" " -f3- $f > "$OUT_DIR/out_${f##*/}"
done
