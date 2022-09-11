# Assignment 1: Genome Assembly

## Question 1
1. $1 \ Mbp * 5 = 5\ Mbp$ needed for 5x coverage. With 100 bp reads, that means $5\ Mbp / 100\ bp = 5\*10^4$ reads. For 15x coverage, we would need that times 3, so $1.5\*10^5$ reads.
2. Code is in `q1_2.py`. Image is saved in `q1_2.png`. 
3. With the random seed of 25, and tweaking the histogram so that the bins are centered around the whole integer coverages, I see that about 0.6\% of the genome has 0 coverage. From visual inspection of the plot, it seems to match Poisson expectations quite well. Printing out the exact values, I get 0.68\% with no coverage from the histogram, 0.67\% from Poisson.
4. Repeating with 15x coverage. Code saved in `q1_4.py`. I modified `q1_2.py` so that they have functions that I can import into this question's file. 0.0009\% of the genes have no coverage. Poisson predicts 0.000031\% with no coverage. 

## Question 2
1. Due to the issue with spades, I had to install a new version and therefore ran this command: `~/Downloads/SPAdes-3.15.5-Darwin/bin/spades.py  --pe1-1 frag180.1.fq --pe1-2 frag180.2.fq --mp1-1 jump2k.1.fq --mp1-2 jump2k.2.fq -o asm_q2 -t 4 -k 31`. Upon running `grep -c '>' asm_q2/contigs.fasta`, I found that 4 contigs had been produced. 
2. I saw in the `contigs.fasta` file that the length of each contig was reported. I used the grep command without any flags and found that the contigs had lengths 105830, 47860, 41351, and 39426. Total length was 234467. The SPAdes documentation (http://cab.spbu.ru/files/release3.12.0/manual.html#sec3.5) also confirmed that the number I found was the sequence length. 
3. The size of my largest contig was 105830 nucleotides.
4. The contig N50 size is defined as the size of the contig that covers at least half of the total genome length. Based on the SPAdes output, the half length of the genome is $234467/2=117233.5$, so I want the contig covering the 117234th position. This is the 2nd contig, with length 47860.

