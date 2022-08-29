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


