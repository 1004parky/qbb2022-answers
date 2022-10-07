
for file in ./*.bam; do 
 if [ -e "$file" ] ; then   # Check whether file exists.
  name=${file%.*}
  name=${name#./}
  echo ${name}
  # STEP 1
  samtools view -q 10 -b -o ${name}_filt.bam ${file}
 fi
done

# STEP 2
# According to https://doi.org/10.1186/gb-2009-10-10-r112, mouse chrom 17 is 95 Mb in length, so 95e6
macs2 callpeak -t D2_Sox2_R1_filt.bam -c D2_Sox2_R1_input_filt.bam -g 94987271 -B -n D2_Sox2_R1
macs2 callpeak -t D2_Sox2_R2_filt.bam -c D2_Sox2_R2_input_filt.bam -g 94987271 -B -n D2_Sox2_R2

# STEP 3
bedtools intersect -a D2_Sox2_R1_peaks.narrowPeak -b D2_Sox2_R2_peaks.narrowPeak -wa > Sox2_intersect.narrowPeak

# STEP 4
bedtools intersect -a Sox2_intersect.narrowPeak -b D2_Klf4_peaks.bed -wa > Klf4_Sox2_intersect.bed
wc -l Klf4_Sox2_intersect.bed
wc -l Sox2_intersect.narrowPeak
wc -l D2_Klf4_peaks.bed

# STEP 5
for file in ./*.bdg; do 
 if [ -e "$file" ] ; then   # Check whether file exists.
  name=${file%.*}
  name=${name#./}
  echo ${name}
  python ~/cmdb-quantbio/assignments/lab/ChIP-seq/extra_data/scale_bdg.py ${file} ${name}_scaled.bdg
  awk '{ if ($2 < 35507055 && $3 > 35502055) print $0 }' ${name}_scaled.bdg > ${name}_scaled_cropped.bdg
 fi
done

### PART 2
curl https://meme-suite.org/meme/meme-software/Databases/motifs/motif_databases.12.23.tgz --output motif_databases.12.23.tgz
# in (base)
sort -k5,5rn Sox2_intersect.narrowPeak | head -300 | awk '{ printf "%s:%i-%i\n", $1, $2, $3 }' > Sox2_intersect_sorted.narrowPeak
samtools faidx -r Sox2_intersect_sorted.narrowPeak -o peak_seq.fasta  mm10.fa
# in (meme)
meme-chip -maxw 7 peak_seq.fasta 
tomtom memechip_out/combined.meme motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme

motif_databases/MOUSE/HOCOMOCOv11_full_MOUSE_mono_meme_format.meme
