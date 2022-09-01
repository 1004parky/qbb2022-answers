This looks great! A very well written solution with good documentation :)

Good question about alternating line lengths for bed files. This is in fact [not allowed](https://genome.ucsc.edu/FAQ/FAQformat.html#format1) and is a good thing to check for in any bed parser. Bedtools would likely throw an error if you tried to give it a file with inconsistent column numbers - the official rules are that if you have a column where only some records have information, the rest of the records should fill in a `.` for that column.

It is interesting that the median # of exons per gene is so low, right? Kind of curious about what this distribution would look like if we plotted it as a histogram.
