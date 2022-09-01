#!/usr/bin/env python
# Yein Christina Park
# Updated 08/31/2022
# Day 3 HW exercise 3
# read in PCA from plink and plot, using metadata to color data

import numpy as np 
import matplotlib.pyplot as plt 

data = np.genfromtxt('eigenvec_metadata.txt', dtype=None, encoding=None)
assert(len(data) == 2548) # should have 2548 points

# separate numeric and relevant label data
category_names = 'population superpopulation gender'.split()
ftag = 'a b c'.split() # for naming files later
categories = np.array([[t[1], t[2], t[3]] for t in data])
pcs = np.array([[t[-2], t[-1]] for t in data]) # separate out pcs data

# ID pop superpop gender pc1 pc2 pc3
for i in range(3):
	# for each metadata type
	for j in set(categories[:,i]): 
		# for each unique category, get plot pcs value
		extract = pcs[np.where(categories[:,i] == j)]
		plt.scatter(extract[:,0], extract[:,1], marker='.', label=j, alpha=0.7)

	plt.legend(prop={'size': 6}, ncol=5)
	plt.title(f'PC1 vs PC2 color coded by {category_names[i]}')
	plt.ylabel('PC2')
	plt.xlabel('PC1')
	plt.tight_layout()
	plt.savefig(f'ex3_{ftag[i]}.png')
	plt.show()

