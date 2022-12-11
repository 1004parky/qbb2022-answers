### Homework 10 Week 14

## Step 1
Modified given code such that it takes a directory and converts all `*.kraken` files in that directory. Did `python convert.py metagenomics_data/step0_givendata/KRAKEN/` to run.

c. `ktImportText -q -o metagenomics_data/step0_givendata/KRAKEN/step1.html metagenomics_data/step0_givendata/KRAKEN/*.txt`

*Question 1*
Actinobacteria population changes a lot through the first week. High, then low, then high again at the end. 

## Step 2
*Question 2* 
"GC-content, tetra-mer composition, and/or co-abundance feature of the contigs across multiple samples" (https://genomebiology.biomedcentral.com/articles/10.1186/s13059-022-02626-w). Perhaps also sequence similarity to different taxonomies? 
a. `bwa index assembly.fasta` in the `step0_givendata` folder.
b. 
```
files="READS/SRR492183 READS/SRR492188 READS/SRR492190 READS/SRR492194 READS/SRR492186 READS/SRR492189 READS/SRR492193 READS/SRR492197"
for file in ${files}; do
    echo ${file}
    #bwa mem -t 4 assembly.fasta ${file}_1.fastq ${file}_2.fastq > ${file}.bam
    samtools sort -o ${file}_sorted.bam ${file}.bam
done
```
c. and d. In the `READS` folder:
```
cp ~/miniconda3/envs/metabat2/lib/libdeflate.so ~/miniconda3/envs/metabat2/lib/libdeflate.0.dylib
conda activate metabat2
jgi_summarize_bam_contig_depths --outputDepth depth.txt *_sorted.bam
metabat2 -i ../assembly.fasta -a depth.txt -o bins
```
*Question 3*
a. 6 bins (8 bins in the given data... not sure why I get such different answers. Maybe random seed?)
b. `15606046/38708237` is `40%`
```
grep -v '>' ../assembly.fasta | wc 
-->  636551  636551 38708237
grep -v '>' bin* | wc 
--> 219884  219884 15606046
```
Note: If I use the bin files given to us in `step3_givendata`, I actually get `21391110` --> `55%` coverage.
c. According to NIH most prokaryotic genomes are less than 5Mb in size. I did the grep and wc command above for each bin file individually and found the lengths were: `2750133, 2289418, 1683638, 1248387, 2525062, 2910568` which all seems right for prokaryotes. 
Note: using the bin files given to us, I get `2157993, 1810927, 2540079, 2910568, 2259886, 2757538, 1683638`. Still reasonable. 
d. Taxonomy; BLAST to known sequences and see how the lengths of genomes compare; look for known essential genes (e.g. polymerase or ribosomes) and determine if you have them present in your bins. 

## Step 3
From NIH taxonomy website (https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?mode=Info&id=1570339) it appears that the kraken classification follows:
`__; ___; superkingdom; clade; phylum; class; order; family; genus; species; strain.`
Using a python script I will be keeping track of the genus and species. 
Code is in `predict_taxonomy.py`. I had planned on using the bin files given to us, but I ran into issues of the IDs found in the bin files NOT appearing in the kraken assembly. So I'm just going to use my 6 bin files. 
*Question 4* 
a. Predictions for bin: (genus, species)
	1. Staphylococcus, Staphylococcus aureus
	2. Staphylococcus, Staphylococcus epidermidis
	3. Anaerococcus, Anaerococcus prevotii
	4. Staphylococcus, Staphylococcus haemolyticus
	5. Cutibacterium, Cutibacterium avidum
	6. Enterococcus, Enterococcus faecalis
b. BLAST.  