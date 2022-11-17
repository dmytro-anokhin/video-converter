#!/bin/bash

files=`ls $1`
`mkdir out`

for filename in $files; do
    echo "$filename"
    `avconvert -s $filename -o out/$filename -p PresetHEVCHighestQuality -prog`
done