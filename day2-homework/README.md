# QBB2022 - Day 2 - Homework Excercises Submission

## Exercise 2
Output from running my script:
```
There were 24 malformed entries
101 records did not have matching IDs in second file.
```
So there were 101 records.

I had implemented a check when creating the position to ID dictionary that checked to make sure the IDs were not overwritten. I learned that the same pos can have different IDs based on the reference allele and/or the alternate allele, so I decided to change the code to create a mapping between (pos, ref, alt) and the ID.

Actually, I decided to add an option for the user to specify whether they wanted to be robust and use all three data points or just use the pos and suppress any ID overwrites.


