#!/bin/bash

# Step 1
#bwa index sacCer3.fa

#for file in ./A01_*.fastq; do 
#  if [ -e "$file" ] ; then   # Check whether file exists.
#		name=${file%.*}
#		name=${name#./}
#		echo ${name}
#		# Step 2
#		bwa mem -R "@RG\tID:${name}\tSM:${name}" -t 4 sacCer3.fa ${file} > aln-${name}.sam
#		# Step 3a
#		samtools sort -@4 -o ${name}.bam aln-${name}.sam
#		# Step 3b
#		samtools index ${name}.bam > ${name}.bam.bai
#  fi
#done

bams=""
for file in ./*.bam; do 
	bams="${bams} ${file}"
done
echo $bams
# Step 4 + 5
freebayes -f sacCer3.fa --genotype-qualities ${bams} | vcffilter -f "QUAL > 20" > yeast_filtered.vcf

vcfallelicprimitives -k -g yeast_filtered.vcf > yeast_ap.vcf

# Step 7
snpeff ann R64-1-1.99 yeast_ap.vcf > snpeff_ann.vcf
