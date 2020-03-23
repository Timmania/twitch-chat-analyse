#!/bin/bash
DIR=$1
BASE=$(basename $DIR)
OUT_DIR="$DIR/out_$BASE"

mkdir $OUT_DIR

# removes all messages from Moobot and Nightbot and removes the timestap and user
for f in $1/*.txt
do
	grep -vi "<moobot>\|<nightbot>" $f |  cut -d" " -f3- > "$OUT_DIR/out_${f##*/}"
done
