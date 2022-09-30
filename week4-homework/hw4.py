import numpy as np 
import matplotlib.pyplot as plt 

# Q2, plot PC1 vs PC2
eigenvecs = np.genfromtxt('plink.eigenvec')

plt.plot(eigenvecs[:,2], eigenvecs[:,3], 'o')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('PC1 vs PC2 for genotypes')
plt.savefig('hw4.2.png')
plt.show()

# Q3 Hist of allele freq
af = np.genfromtxt('plink.frq')
plt.hist(af[1:,4])
plt.xlabel('Allele frequency')
plt.ylabel('Counts')
plt.title('Histogram of allele frequencies')
plt.savefig('hw4.3.png')
plt.show()

# Q5
files = ['plink.GS451_IC50.assoc.linear', 'plink.CB1908_IC50.assoc.linear']
for f in files:
	pvals = np.genfromtxt(f)[1:, -1] # Only keep pvals
	xs = np.arange(len(pvals))

	name = f.split(".")[1]

	# Select pvals less than 1e-5
	sig_ps = pvals[np.where(pvals < 1e-5)]
	sig_xs = xs[np.where(pvals < 1e-5)]
	
	plt.plot(xs, -np.log(pvals), '.')
	plt.plot(sig_xs, -np.log(sig_ps), '.', label='Significant')
	plt.legend()
	plt.xlabel('SNP index')
	plt.ylabel('-log(P) from linear association test')
	plt.title(f'Manhattan plot for {name} phenotype')
	plt.savefig(f'hw4.5_{name}.png')
	plt.show()

# Q6
# choosing GS451_IC50
# get top SNP, do boxplot of phenotype
data = np.genfromtxt('plink.GS451_IC50.assoc.linear', dtype=str)[1:]
pvals = data[:,-1].astype(float)
snp_id = data[np.argmax(-np.log(pvals)),1]

with open('gwas_data/genotypes.vcf', 'r') as f:
	for line in f:
		if line.startswith('#'):
			if line.startswith('#CHROM'):
				id_row = line.split()
		elif line.split()[2] == snp_id:
			# Data rows
			snp_row = line.split()
			break 

col2val = dict(zip(id_row, snp_row))
ref = col2val['REF'] # Corresponds to 0
alt = col2val['ALT']

# parse phenotype files
phenotypes = np.genfromtxt('gwas_data/GS451_IC50.txt')[1:]
id2pheno = dict() # take 1001_1001 --> phenotype value
for row in phenotypes:
	id2pheno['_'.join(row[0:2].astype(int).astype(str))] = row[-1]

# Need to get allele 
sample_ids = id_row[9:] # these will be 1001_1001, etc. 
hom0 = []
het = []
hom1 = []

for sample in sample_ids:
	genotype_str = col2val[sample]
	if genotype_str == '0/1' or genotype_str == '1/0':
		if not np.isnan(id2pheno[sample]): het.append(id2pheno[sample])
	elif genotype_str == '1/1':
		if not np.isnan(id2pheno[sample]): hom1.append(id2pheno[sample])
	elif genotype_str == '0/0':
		if not np.isnan(id2pheno[sample]): hom0.append(id2pheno[sample])

plt.boxplot([hom0, het, hom1], labels=[f'{ref}{ref}',f'{ref}{alt}',f'{alt}{alt}'])
plt.xlabel('Genotype')
plt.ylabel('Phenotype effect')
plt.title('Boxplots of phenotype effect by genotype')
plt.savefig('hw4.6.png')
plt.show()

# For 7
for f in files:
	data = np.genfromtxt(f, dtype=str)[1:]
	pvals = data[:,-1].astype(float)
	snp_id = data[np.argmax(-np.log(pvals)),1]
	print(f'Most significant association SNP ID for {f}: {snp_id}')