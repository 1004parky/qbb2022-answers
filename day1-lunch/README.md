# QBB2022 - Day 1 - Lunch Exercises Submission

1. I’m excited to learn better documentation

2. 
b. The mean number of exons per gene is 62.
The code I used: 
```
$ wc -l genes.chr21.bed
$ wc -l exons.chr21.bed
$ echo $((13653/219))
```
c. To find the median, we have to get a list of the number of exons for each gene. Save to a new file. Then sort the list in numeric order (e.g. sort -n), and find the middle of the list. Since there are 219 genes, we know we're looking for the 110th value. You could scroll to find the value, or do a combination of head -110 | tail -1. Or you could use awk.


