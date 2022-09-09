# Assignment 1: Genome Assembly

## Question 1
1. $1 \ Mbp * 5 = 5\ Mbp$ needed for 5x coverage. With 100 bp reads, that means $5\ Mbp / 100\ bp = 5\*10^4$ reads. For 15x coverage, we would need that times 3, so $1.5\*10^5$ reads.
2. Code is in `q1_2.py`. Image is saved in `q1_2.png`. 
3. With the random seed of 25, and tweaking the histogram so that the bins are centered around the whole integer coverages, I see that about $0.6\%$ of the genome has 0 coverage. From visual inspection of the plot, it seems to match Poisson expectations quite well. Printing out the exact values, I get $0.68%$ with no coverage from the histogram, $0.67\%$ from Poisson.
4. Repeating with 15x coverage. Code saved in `q1_4.py`. I modified `q1_2.py` so that they have functions that I can import into this question's file. $0.0009\%$ of the genes have no coverage. Poisson predicts $0.000031\%$ with no coverage. 
