vcf=~/data/vcf_files/random_snippet.vcf
bed=~/data/bed_files/chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed

awk '{if($4==1||$4==2){print}}' $bed > states12.bed 

bedtools intersect -a $vcf -b "states12.bed" | awk '{if ($4 == "C") {print $5}}' | sort | uniq -c

