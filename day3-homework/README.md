# QBB2022 - Day 3 - Homework Exercises Submission

## Exercise 1 
I mainly used the main plink documentation website and gleaned that it was a command-line command, with --vcf file and --pca flags. I had actually impulsively gunzip'd the provided data file into a vcf file but after learning that plink can also accept `*.gz` files, I removed my unzipped file (because wow it was much larger than the zipped file)

```
plink --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz --pca
PLINK v1.90b6.21 64-bit (19 Oct 2020)          www.cog-genomics.org/plink/1.9/
(C) 2005-2020 Shaun Purcell, Christopher Chang   GNU General Public License v3
Logging to plink.log.
Options in effect:
  --pca
  --vcf ALL.chr21.shapeit2_integrated_v1a.GRCh38.20181129.phased.vcf.gz

16384 MB RAM detected; reserving 8192 MB for main workspace.
--vcf: plink-temporary.bed + plink-temporary.bim + plink-temporary.fam written.
976599 variants loaded from .bim file.
2548 people (0 males, 0 females, 2548 ambiguous) loaded from .fam.
Ambiguous sex IDs written to plink.nosex .
Using up to 8 threads (change this with --threads).
Before main variant filters, 2548 founders and 0 nonfounders present.
Calculating allele frequencies... done.
976599 variants and 2548 people pass filters and QC.
Note: No phenotypes present.
Relationship matrix calculation complete.
--pca: Results saved to plink.eigenval and plink.eigenvec .
```
I wasn't really sure what options to specify so I had just run sort of blind. Looking at the results, which pulled the top 20 eigenvalues, if I had to rerun, I would probably run with just 2 principal components because they have eigenvalues an order of magnitude greater than the rest of the eigenvalues. 

## Exercise 2
For this part I actually had to conda install numpy which I've never had to do before? Idk if that was right that I didn't already have numpy loaded. Actually, I had to install openblas.

I do notice very apparent patterns formed between the two PCs plotted. They aren't simply linear correlations or anything, but clear clusters or regions of linear correlation.


