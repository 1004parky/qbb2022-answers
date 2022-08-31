#!/usr/bin/env python
# Yein Christina Park
# Updated 08/31/2022
# Day 3 HW exercise 2 
# read in PCA from plink and plot

import numpy as np 
import matplotlib.pyplot as plt 

eigenvectors = np.genfromtxt('plink.eigenvec')[:,2:5] # only need 3 numerical rows

assert(len(eigenvectors) == 2548) # should have 2548 points

plt.scatter(eigenvectors[:,0], eigenvectors[:,1])
plt.title('chr21 data PCA scatter PC1 vs PC2')
plt.ylabel('PC2')
plt.xlabel('PC1')
plt.savefig('ex2_a.png')
plt.show()

plt.scatter(eigenvectors[:,1], eigenvectors[:,2])
plt.title('chr21 data PCA scatter PC2 vs PC3')
plt.ylabel('PC3')
plt.xlabel('PC2')
plt.savefig('ex2_b.png')
plt.show()