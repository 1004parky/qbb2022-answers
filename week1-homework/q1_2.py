import numpy as np 
import matplotlib.pyplot as plt 
import random 
import math  
import scipy.special 

# Simulate sequencing 5x coverage of 1Mbp with 100 bp reads
# Plot hist of coverage

# Random start position, uniform probability; positions 1 through 999,901
# Record array of 1M positions

# Overlay hist with Poisson dist with lambda 5

def simulate(len_genome, c, len_r):
	'''
	Given length of genome, the desired coverage, and the length of reads,
	Randomly sample from uniform distribution appropriate number of reads
	'''
	genome = np.zeros(int(len_genome))
	nreads = int(len_genome*c/len_r)

	for i in range(nreads):
		start = random.randint(0, len_genome-len_r) # randint is inclusive for lower and upper limit
		genome[start:start+len_r] += 1

	return genome 

def plot_compare(genome, c, fname, title='Simulated and theoretical 5x coverage of 1Mbp with 100 bp reads'):
	'''
	Given genome (number of sequences for each position of genome) and c, the coverage
	Plot histogram for genome, and poisson with lambda c. fname is what file name to save picture. 
	'''
	n, bins, _ = plt.hist(genome, density=True, label='Coverage', bins=np.arange(-0.5, np.max(genome)+1, 1))

	xs = np.arange(0, np.max(bins), 0.1) # base on xrange of histogram
	# scipy factorial takes list as input too 
	poisson = np.exp(-c)*np.power(c, xs)/scipy.special.factorial(xs)
	plt.plot(xs, poisson, '.-', label='Poisson')

	print(n[0], poisson[0])

	plt.legend()
	plt.title(title)
	plt.xlabel('Coverage')
	plt.ylabel('Frequency')
	plt.savefig(f'{fname}.png')
	plt.show() 


if __name__ == '__main__':
	random.seed(25) # set one seed 
	genome = simulate(1e6, 5, 100)
	plot_compare(genome, 5, 'q1.2')

