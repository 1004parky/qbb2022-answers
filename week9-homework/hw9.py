import numpy as np 
import matplotlib.pyplot as plt 
import scipy
import statsmodels.api as sm 

from scipy.cluster.hierarchy import linkage, dendrogram, leaves_list
from statsmodels.formula.api import ols 
from statsmodels.stats.multitest import multipletests

# Read in data
input_arr = np.genfromtxt("dros_gene_expression.csv", delimiter=',', names=True, dtype=None)
col_names = list(input_arr.dtype.names)
t_names = []
expr_data = []

for row in input_arr:
	t_names.append(row[0].decode('utf-8'))
	expr_data.append(list(row)[1:])

t_names = np.array(t_names)
expr_data = np.array(expr_data)

# Subset to only transcripts whose med expr > 0
t_names_subset = t_names[np.where(np.median(expr_data, axis=1) > 0 )]
expr_data_subset = expr_data[np.where(np.median(expr_data, axis=1) > 0 )]

# Transform data
expr_data_subset_proc = np.log2(expr_data_subset + 0.1)

# Step 1: clustering
# I did not do the structured_to_unstructured thing because I determiend that my expr_data_subset_proc is the same
# 1.1 Cluster data 

# Z = linkage(expr_data_subset_proc, 'ward')
# fig = plt.figure(figsize=(10, 5))
# dn = dendrogram(Z, labels=None)
# row_order = leaves_list(Z)
# plt.title('Dendrogram of genes')
# plt.xlabel("Gene")
# plt.tight_layout()
# plt.savefig('dendrogram_genes.png')
# plt.close()

# Z = linkage(expr_data_subset_proc.T, 'single')
# col_order = leaves_list(Z)
# fig = plt.figure(figsize=(10, 5))
# dn = dendrogram(Z, labels=list(input_arr.dtype.names)[1:])
# plt.title('Dendrogram of samples')
# plt.xlabel("Sample")
# plt.tight_layout()
# plt.savefig('dendrogram_samples.png')
# plt.close()

# row_sorted = expr_data_subset_proc[row_order, :]
# full_sorted = row_sorted[:, col_order]
# plt.imshow(full_sorted, aspect='auto', cmap='magma')
# plt.colorbar()
# plt.title('Heatmap of gene expression')
# plt.xlabel('Sample')
# plt.ylabel('Gene')
# plt.tight_layout()
# plt.savefig('heatmap.png')
# plt.close()

# Step 2 
# least squares regression
# Use stage number as numeric indpendent variable (10, 11, 12, 13, 14)
sexes = [c.split('_')[0] for c in col_names[1:]]
stages = [int(c.split('_')[1]) for c in col_names[1:]]

slopes = []
pval_slopes = []

for i in range(expr_data_subset_proc.shape[0]):
	# for each gene
	list_of_tuples = []
	for j in range(1, len(col_names)):
		# columns are gene name, samples.
		list_of_tuples.append((t_names_subset[i],expr_data_subset_proc[i,j-1], sexes[j-1], stages[j-1]))
	longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])

	result = ols('fpkm ~ stage', longdf).fit()
	slopes.append(result.params['stage'])

	pval_slopes.append(result.pvalues['stage'])

sm.qqplot(np.array(pval_slopes), dist=scipy.stats.uniform, line='45')
plt.title('QQ plot vs uniform dist')
plt.legend(['Data', 'Uniform distribution'])
plt.savefig('qqplot.png')
plt.close()

significant_idx = multipletests(pval_slopes, alpha=0.1, method='fdr_bh')[0]
diff_stage = t_names_subset[significant_idx]
np.savetxt('diff_transcripts_stage.txt', diff_stage, fmt='%s', header='List of differentially expressed transcripts (10% FDR, by stage only, no sex covariate)')

# Repeat controlling sex as covariate
slopes = []
pval_slopes = []
for i in range(expr_data_subset_proc.shape[0]):
	# for each gene
	list_of_tuples = []
	for j in range(1, len(col_names)):
		# columns are gene name, samples.
		list_of_tuples.append((t_names_subset[i],expr_data_subset_proc[i,j-1], sexes[j-1], stages[j-1]))
	longdf = np.array(list_of_tuples, dtype=[('transcript', 'S11'), ('fpkm', float), ('sex', 'S6'), ('stage', int)])

	result = ols('fpkm ~ stage + sex', longdf).fit()
	slopes.append(result.params['stage'])

	pval_slopes.append(result.pvalues['stage'])

slopes = np.array(slopes)
pval_slopes = np.array(pval_slopes)

significant_idx = multipletests(pval_slopes, alpha=0.1, method='fdr_bh')[0]
diff_stage_sex = t_names_subset[significant_idx]
np.savetxt('diff_transcripts_stage_sex.txt', t_names_subset[multipletests(pval_slopes, alpha=0.1, method='fdr_bh')[0]], fmt='%s', header='List of differentially expressed transcripts (10% FDR, by stage only, with sex as covariate)')

overlap = len(list(set(diff_stage_sex) & set(diff_stage)))
print(f'Percent overlap: {overlap/len(diff_stage)*100}')

# volcano plot
plt.plot(slopes, -np.log10(pval_slopes), '.b', label='Not significant')
plt.plot(slopes[significant_idx], -np.log10(pval_slopes[significant_idx]), '.r', label='significant')
plt.title('Volcano plot by stage with sex as covariate')
plt.xlabel('Beta for stage')
plt.ylabel('-log10(p value)')
plt.legend()
plt.savefig('volcano.png')