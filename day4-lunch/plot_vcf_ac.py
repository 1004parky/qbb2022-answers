#!/usr/bin/env python3

import sys
import matplotlib.pyplot as plt

vcf = sys.argv[1]
fs = open( vcf )

ac = []
for i, line in enumerate( fs ):
    if "#" in line:
        continue
    fields = line.split()
    info = fields[7].split(";")
    ac.append( int(info[0].replace("AC=","")) )

fig, ax = plt.subplots()
ax.hist( ac, density=True, log=True)
ax.set_title(f'Histogram for {vcf}')
ax.set_ylabel('Frequency')
ax.set_xlabel('Allele count')
ax.set_ylim((4e-6,3e-3)) # after manual inspection of data
fig.tight_layout()
fig.savefig( vcf + ".png" )

fs.close()

