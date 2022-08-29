# QBB2022 - Day 1 - Lunch Exercises Submission

1. I’m excited to learn better documentation

2. 
	b. The mean number of exons per gene is 62.3
	The code I used: 
	```
	$ wc -l genes.chr21.bed
	$ wc -l exons.chr21.bed
	$ echo $((13653/219)) --> this gives you integers only though
	```
	c. To find the median, we have to get a list of the number of exons for each gene. Save to a new file. Then sort the list in numeric order (e.g. sort -n), and find the middle of the list. Since there are 219 genes, we know we're looking for the 110th value. You could scroll to find the value, or do a combination of head -110 | tail -1. Or you could use awk.

3. 
	b. Command used: 
	```
	sort -nk 4 chromHMM.E116_15_coreMarks_hg38lift_stateno.chr21.bed | uniq -cf 3 | cut -f 1,4
	```

	```
	Tally:
	 305 chr21	1
	 678 chr21	2
	  79 chr21	3
	 377 chr21	4
	 808 chr21	5
	 148 chr21	6
	1050 chr21	7
	 156 chr21	8
	 654 chr21	9
	  17 chr21	10
	  17 chr21	11
	  30 chr21	12
	  62 chr21	13
	 228 chr21	14
	 992 chr21	15
	```

	We used cut to just clean up the output a little bit.

	c. For each state, we would want to look at the cumulative lengths of the genes; we can get the gene lengths by subtracting the start position from the end position. Every gene belongs to a state, so then I would keep track of 15 total sums (one for each state), and add the length to the correct tracked number. The state with the largest total sum would be the state with the largest fraction of the genome. (You could use sort -n and tail -1 to find the largest in the list). We'd have to make sure to keep track of which column/number corresponds to which state; we could make "state" an additional column in the sums file.

4. b. 
	```
	grep "AFR" integrated_call_samples.panel | sort -k 2 | cut -f-3 | uniq -cf 1
	```
	```
	 123 HG01880	ACB	AFR
	 112 NA19625	ASW	AFR
	 173 HG02922	ESN	AFR
	 180 HG02462	GWD	AFR
	 122 NA19017	LWK	AFR
	 128 HG03052	MSL	AFR
	 206 NA18484	YRI	AFR
	```
 	c. You could change the grep keyword for each superpopulation. Or, you could try something like this (sort by population and super-population at the same time): `sort -k 2,3 integrated_call_samples.panel | cut -f -3 | uniq -cf 1`

5. b. Command used: `cut -f 1-9,13 random_snippet.vcf > HG00100.vcf`
	c. Command used: `cut -f 10 HG00100.vcf | sort | uniq -c`
	```
	9514 0|0
	127 0|1
	178 1|0
	181 1|1
	```

	d.  Using `grep -wc "AF=1" HG00100.vcf` we see that there are 15 rows with an exact match with `AF=1`. There are 34 rows where the phrase `AF=1` appears at least once in the row, but this can be misleading because there are categories like `EUR_AF` or `AFR_AF`.
	e. Upon visual inspection, there are six total parameters ending in AF, so theoretically `AF=1` could appear 6 times in each line.
	f. To extract the AFR values, you would cut just that column (column 8), then use cut again with the delimiter options `-d ";" -f 7` to get just the `AFR_AF` parts.  Then you could cut again with options `-d "=" -f 2` to give you just the values. Also to make things cleaner, we could get rid of all the comment lines by doing inverse grep (`grep -v "#"`) before running all the cut functions.

