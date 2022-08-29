#!/bin/bash

#USAGE: bash exercise1.sh input_VCF

for nuc in A C G T
do
  echo "Considering " $nuc
  awk '/^#/{next} {if ($4 == nuc) {print $5}}' nuc="$nuc" $1 | sort | uniq -c 
  # OR:  awk -v nuc="$nuc" '/^#/{next} {if ($4 == nuc) {print $5}}'
done
