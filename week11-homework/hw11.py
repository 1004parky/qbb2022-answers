import scanpy as sc

# Read 10x dataset
adata = sc.read_10x_h5("neuron_10k_v3_filtered_feature_bc_matrix.h5")
# Make variable names (in this case the genes) unique
adata.var_names_make_unique()

# Normalization and filtering as of [Zheng17]
adata_filt = sc.pp.recipe_zheng17(adata, copy=True)

# PCA before and after filtering
sc.tl.pca(adata)
sc.tl.pca(adata_filt)

# sc.pl.pca(adata, title='PCA before filtering', save='_before.png')
# sc.pl.pca(adata_filt, title='PCA after filtering', save='_after.png')

# Clustering with leiden
sc.pp.neighbors(adata_filt)
sc.tl.leiden(adata_filt)

sc.tl.tsne(adata_filt)
sc.tl.umap(adata_filt, maxiter=1000)

#sc.pl.umap(adata_filt, title='Clusters with UMAP', save='_umap.png', color='leiden')
#sc.pl.tsne(adata_filt, title='Clusters with tSNE', save='_tsne.png', color='leiden')

# Step 3: Distinguish 
adata_filt_ttest = sc.tl.rank_genes_groups(adata_filt, 'leiden', method='t-test', copy=True)
#sc.pl.rank_genes_groups(adata_filt_ttest, n_genes=25, sharey=False, title='t-test rank genes groups', save='_ttest.png')

adata_filt_log = sc.tl.rank_genes_groups(adata_filt, 'leiden', method='logreg', copy=True)
#sc.pl.rank_genes_groups(adata_filt_log, n_genes=25, sharey=False, title='Logistic rank genes groups', save='_logreg.png')

# Step 4: Cell steps
# Get all gene names

# Look at a bunch of candiate genes to identify which ones can distinguish genes
# genes = adata_filt.var.index
# for i in range(0, len(genes), 10):
# 	# Look at every tenth gene
# 	sc.pl.umap(adata_filt, color=[genes[i], 'leiden'])


# create a dictionary to map cluster to annotation label
cluster2annotation = {
     '26': 'Microglia',
     '9': 'Fibroblast-like type 1',
     '16': 'Red blood cells',
     '24': 'EC cells',
     '25': 'Smooth Muscle Cells',
     '23': 'aEC cells'
}
adata_filt.obs['cell type'] = adata_filt.obs['leiden'].map(cluster2annotation).astype('category')
sc.pl.umap(adata_filt, color='cell type', legend_loc='on data',
           frameon=False, legend_fontsize=10, legend_fontoutline=2, save='cell_labels.png')
