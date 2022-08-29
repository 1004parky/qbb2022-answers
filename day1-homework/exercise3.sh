#!/bin/bash

#USAGE: bash exercise3.sh input_VCF

awk -v OFS='\t' '/^#/{next} {print $1,$2-1,$2}' $1 | sort -k1,1 -k2,2n > variants.bed
sort -k1,1 -k2,2n ~/data/bed_files/genes.bed > genes.sorted.bed
bedtools closest -a variants.bed -b genes.sorted.bed > e3.out 

