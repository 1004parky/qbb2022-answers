# QBB2022 - Day 4 - Lunch Exercises

## Exercise 1
I cloned the `cmdb-plot-vcfs` to my home directory. This is the output reporting the bp covered:
```
*** Subsetting .vcf for each feature
--- Subsetting exons.chr21.bed.vcf
    + Covering 1107407 bp
--- Subsetting processed_pseudogene.chr21.bed.vcf
    + Covering 956640 bp
--- Subsetting protein_coding.chr21.bed.vcf
    + Covering 13780687 bp
```

You could use the `cmp` or `diff` functions in bash... actually, for pictures I think it stores when they were made or modified... so I found the imagemagick `compare` function I could install, or on mac, the `pdiff` tool I could also install.

I don't know if this is the intention, but the gtf file is really hard to read through... I would like to extract just gene type types. I used awk to do this: `awk '{for (i=1; i <=NF; i++) {if($i=="gene_type") print $(i+1)}}'`. However there were so many types that sorting and then doing uniq was very slow. I just used `less` on the `awk | uniq` output and looked through manually.

We had looked at exons, protein coding, and processed pseudogene. There were also miRNA, lncRNA, and transcribed unprocessed pseudogene. I know miRNA is important in regulation, too; for long non-coding RNA, I'm not as sure of the functional role, but the fact that the gene is being transcribed, at least, sounds important. Same for the last category, I'm not sure what a pseudogene is, but the fact that it is transcribed indicates that thy may have some implications in disease or physiology.

## Exercise 2

