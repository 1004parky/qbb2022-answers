# QBB2022 - Day 1 - Homework Exercises Submission

## Exercise 1
- Running the command `source exercise1.sh ~/data/vcf_files/random_snippet.vcf` I see these errors:
```
Considering  A
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  C
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  G
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  T
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
```
I decided to google `awk: illegal field $()`. Stack overflow told me that I needed to define variables outside awk with a `-v` flag or define it after awk. So I can change line 8 in the `exercise1.sh` file to define `nuc`.

I also had to get rid of the dollar sign in front of nuc in the awk string because I got another error message (`illegal field $(C), name "nuc"`)

This was my output from the script:
```
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
```
 - I'm not sure whether these make sense... A and G are most associated with each other, and C and T are most associated with each other. THis makes sense because chemically, A and G are purines and C and T are pyrimidines.

## Exercise 2
- All code is in `exercise2.sh`:
```

```
- Deciding which states to consider as promoter-adjacent was not straight-forward. We learned that TSS means transcription start site, so I chose states 1 and 2 as my promoter-like regions.
- We wanted to keep info from the vcf file so used that as `-a` in `bedtools intersect`. In order to get just states 1 and 2, we used awk on the bed file to get just the lines with states 1 and 2.
Output:
```
  12 A
  11 G
  39 T
```
So T is the most common alternate allele.
The most common alternate allele is still T, just like in the entire random snippet, but A and G are more equal here, whereas G was less common an allele in the entire snippet data. That could be significant and could be further probed.

## Exercise 3
- I think this file is printing the the first column, second column value (minus 1), and second column value of the `input_VCF` file and writing all of this out to `variants.bed`. Then, we sort based on the first column alphanumerically and the 2nd column numerically for the `genes.bed` file and write that to another file. Then we find the genes in `genes.sorted.bed` that are closest to the genes listed in `variants.bed` using the bedtools closest tool.
- Error 1:
```
Error: unable to open file or unable to determine types for file variants.bed
```
I googled around and found that there was some issue with the tabs, so I'm going to edit the awk line to replace commas with tabs (`\t`). For this I used the output field separator awk function I found on stack overflow. 
- Error 2:
```
Error: Sorted input specified, but the file variants.bed has the following out of order record
chr21	5218156	5218157
```
This means the sorting did not go as intended. Or rather, the variants file is not sorted. So I added the sort lines to the end of the initial awk line to get a sorted variants file!

- To get the number of variants I used `wc -l e3.out` and I got 10293... We know gene names are in the last column so to get the number of unique genes: `sort -k 7 e3.out | cut -f 7 | uniq -c | wc -l` to get 200 unique genes. So on average there are 10293 divided by 200 so around 51.5 variants per gene.

