import numpy as np 
import matplotlib.pyplot as plt 

# Read in vcf data from snpeff

def parse_vcf(vcf, col, field=None):
	# Specify column index and field name
	data = []
	with open(vcf, 'r') as f:
		for line in f:
			if line.startswith('#'): continue # header
			fields = line.split()
			if field:
				# If user specified field
				things = fields[col].split(';')
				keys = [f.split('=')[0] for f in things]
				values = [f.split('=')[1] for f in things]
				
				# Want to make a dictionary 
				d = dict(zip(keys, values))
				if ',' in d[field]:
					data += d[field].split(',')
				else:
					data.append(d[field])
			else:
				data.append(fields[col])
	f.close()
	return data

def parse_anns(anns):
	types = []
	for a in anns:
		fields = a.split('|')
		# If it ever equals A T C or G, need to count the next one 
		for i in range(len(fields)):
			if fields[i] in 'A T C G'.split():
				if fields[i+1] == '': continue
				types += fields[i+1].split('&')
	return types

# Parse vcf file
vcf = 'snpeff_ann.vcf'

fig, axs = plt.subplots(2,2)

# Read depth distribution is DP
# column index 7 
# AB=0.16129;ABP=33.9012;AC=8;AF=0.4;AN=20;AO=10;CIGAR=1X1M1X;DP=120
dps = np.array(parse_vcf(vcf, 7, 'DP')).astype(int)
axs[0,0].hist(dps, bins=50)
axs[0,0].set_title('Read depth distribution')
axs[0,0].set_ylabel('Counts')
axs[0,0].set_xlabel('Read depth')

# Quality distribution, QUAL? histogram
# index 5 column
quals = np.array(parse_vcf(vcf, 5)).astype(float)
axs[0,1].hist(quals, bins=50)
axs[0,1].set_title('Quality distribution')
axs[0,1].set_ylabel('Counts')
axs[0,1].set_xlabel('Quality distribution')

# Allele frequency AF; histogram 
# column index 7 
# AB=0.16129;ABP=33.9012;AC=8;AF=0.4;AN=20;AO=10;CIGAR=1X1M1X;DP=120
afs = np.array(parse_vcf(vcf, 7, 'AF')).astype(float)
axs[1,0].hist(afs, bins=50)
axs[1,0].set_title('Allele frequency')
axs[1,0].set_ylabel('Counts')
axs[1,0].set_xlabel('Allele frequency')

# bar plot of something INFO field variant type
# ANN=C|upstream_gene_variant|; column 7
anns = parse_anns(parse_vcf(vcf, 7, 'ANN')) # get one of them 
effects = list(set(anns))
freq = [anns.count(e) for e in effects]
print(effects)
axs[1,1].barh(np.arange(len(effects)), freq)
axs[1,1].set_title('Predicted effects')
axs[1,1].set_xlabel('Counts')
axs[1,1].set_ylabel('Effect type')
axs[1,1].set_yticks(np.arange(len(effects)))
axs[1,1].set_yticklabels(effects, fontdict={'fontsize':5})

plt.tight_layout()
plt.savefig('hw3.8.png')
plt.show()
