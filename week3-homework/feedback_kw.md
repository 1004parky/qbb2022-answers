# Week 3 Variant Calling -- Feedback

1 + 1 + 1 + 0.75 + 1 + 1 + 1 + 1 + 1 + 0 = 8.75 points out of 10 possible points

1. Index genome

  * --> +1

2. align reads

  * --> +1
  * nice for loop for q2&3

3. sort bam files and index sorted bam files (0.5 points each)

  * --> +1

4. variant call with freebayes

  * should include the `-p 1` flag since the yeast ploidy is 1.
  * --> +0.75

5. filter variants

  * --> +1

6. decompose complex haplotypes

  * --> +1

7. variant effect prediction

  * --> +1

8. python plotting script

  * --> +1; nice script overall. Would recommend GQ in the Format/sample specific column, not QUAL in column 5. You want the genotype quality and genotypes are sample specific

9. 4 panel plot (0.25 points each panel)

  * --> +1

10. 1000 line vcf

  * I don't see the vcf file. Did you do `git add --force <your.vcf>`?
