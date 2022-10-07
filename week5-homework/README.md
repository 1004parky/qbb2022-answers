## Homework 5

### Part 1
Code is in `hw5.sh`. 

For step 4:
| Desc        | Value       |
| ----------: | :---------- |
| Total peaks Klf4 | 60       |
| Total peaks Sox2   | 593        |
| Overlapping peaks   | 41        |
| Percentage Klf4 peaks colocalized  | 68.3\%  |

Step 5 is in the bash script and continued in `hw5_1.py` (1 stands for the part, not the step)

### Part 2 
`curl https://meme-suite.org/meme/meme-software/Databases/motifs/motif_databases.12.23.tgz --output motif_databases.12.23.tgz`
`tar xzf motif_databases.12.23.tgz`
Again, the commands are in `hw5.sh`

### Part 3
There were two matches:
- `Matches to 1 (GGGTGKG-MEME-1)`
- `Matches to 2 (CYCYKCC-MEME-2)`

`grep 'SOX2\|KLF4' tomtom_out/tomtom.tsv > matches.txt`