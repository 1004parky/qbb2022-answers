import sys 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.stats import pearsonr, kde

fname = 'xpresso_predictions_human.txt' # sys.argv[1]

gene_names = []
k562_model_predictions = []
k562_observations = []
desc = [] # descriptions

for line in open(fname):
    line = line.strip('"')
    if line.startswith('##'):
        # header 
        header = line.strip('\r\n').strip('##').split('\t')
        k562_obs_idx = header.index("E123")
    if not line.startswith('#'):
        fields = line.strip('"\r\n').split('\t')
        gene_names.append(fields[1])
        k562_model_predictions.append(float(fields[4]))
        k562_observations.append(float(fields[k562_obs_idx]))
        desc.append(fields[2])

# extract genes of interest
genesoi = 'PIM1 SMYD3 FADS1 PRKAR2B GATA1 MYC'.split()
genesoilocs =[]
for g in genesoi:
    genesoilocs.append(gene_names.index(g))
for i in range(len(desc)):
    if "hemoglobin subunit" in desc[i]:
        genesoi.append(gene_names[i])
        genesoilocs.append(i)


fig, ax = plt.subplots()
x, y = np.array(k562_model_predictions), np.array(k562_observations)
nbins = 300
# Smooth data
k = kde.gaussian_kde([x, y])
xi, yi = np.mgrid[x.min():x.max():nbins*1j, y.min():y.max():nbins*1j] # 1j means imaginary 
zi = k(np.vstack([xi.flatten(), yi.flatten()]))
# Plot smoothed data
plt.pcolormesh(xi, yi, zi.reshape(xi.shape), shading='auto', cmap=plt.cm.Blues)
ax.set_xlabel("Predicted K562 expression level,\n10-fold cross-validated")
ax.set_ylabel("K562 expression level (log10)")

# Correlation 
corr = pearsonr(k562_model_predictions, k562_observations)
ax.text(.5, 3.75, f"r^2 = {round(corr.statistic**2,2)}\nn = {len(k562_observations)}")
line_xs = np.linspace(max(min(k562_model_predictions), min(k562_observations)), min(max(k562_model_predictions), max(k562_observations)), 100)
line_ys = line_xs
ax.plot(line_xs, line_ys, color = "maroon")

for i, geneoi in enumerate(genesoi):
    ax.text(k562_model_predictions[genesoilocs[i]], k562_observations[genesoilocs[i]], geneoi, color="maroon", fontweight="demi", fontsize=4)

ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)
plt.tight_layout()
plt.savefig('xpresso_3a.png')
plt.show()