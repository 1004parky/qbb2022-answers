import numpy as np 
import matplotlib.pyplot as plt 


# 1: wright-fisher sim
def wright_fisher(af, n_pop):
	# start_af is one starting allele freq
	# allele frequency = fraction of all chrom in pop that have allele
	# There are 2N chromosomes
	if af > 1:
		raise Exception('Allele frequency must be <= 1')

	af_time = [af]
	while 0 < af < 1:
		# Run until one of the alleles becomes fixed
		# Selection step 
		i = af*n_pop*2 # number of alleles
		#pA = i*(1+s)/(2*n_pop - i + i*(1+s))
		# Number of A's in next generation
		new_A = np.random.binomial(n_pop*2, af)
		# update allele frequency based on result
		af = new_A/(2 * n_pop) 
		af_time.append(af)

	return dict({'af': af_time, 'N': n_pop}) 

def plot_af(af_dict, save=None):
	# Step 2. Plot allele freq vs generation number
	# The simulation initial params are stored in af_dict
	# af_dict should be output from write_fisher() function and should
	# contain 'af' and 'N' keys
	af_time = af_dict['af']

	plt.plot(np.arange(len(af_time)), af_time)
	plt.title(f'Allele frequency vs generation number\nStart AF: {af_time[0]}, population size: {af_dict["N"]} ')
	plt.xlabel('Generation')
	plt.ylabel('Allele frequency in population')
	plt.ylim((-0.1,1.1))
	if save:
		plt.savefig(save)
	plt.show()

def run_fixation(n_runs, af, n_pop):
	# Step 3
	# Run wright_fisher n_runs times, and return fixation time for each run
	# This fixation time does NOT include time 0 as a step. 
	fixation = []
	for i in range(n_runs):
		af_dict = wright_fisher(af, n_pop)
		fixation.append(len(af_dict['af']))
	return fixation

# plot_af(wright_fisher(0.5, 10), save='af_1.1.png')
# plot_af(wright_fisher(0.8, 10), save='af_1.2.png')

# # Step 3
# # Histogram for 1000 runs
# af = 0.5
# n_runs = 1000
# n_pop = 100
# plt.hist(run_fixation(n_runs, af, n_pop))
# plt.title(f'Histogram of fixation time for {n_runs} runs\nStart AF: {af}, population size: {n_pop}')
# plt.xlabel('Fixation time (for any allele) (generations)')
# plt.ylabel('Counts')
# plt.savefig('hist_3.png')
# plt.show()

# # Step 4
# # Vary pop size
# af = 0.5
# n_runs = 1 # per condition
# for i in range(2, 8): 
# 	# Will give me n_pop from 100 to 10 million 
# 	n_pop = 10**i
# 	fixation = run_fixation(n_runs, af, n_pop)
# 	plt.plot(n_pop, fixation[0], '.r')
# plt.title(f'Fixation time (for any allele) vs population size\nStart AF: {af}')
# plt.ylabel('Fixation time (for any allele) (generations)')
# plt.xlabel('Population sizes')
# plt.xscale('log')
# plt.yscale('log')
# plt.savefig('fixation_v_size_4.png')
# plt.show()

# Step 5
# vary AF
n_runs = 100 
n_pop = 1000
fixations = []
for af in np.arange(0, 1.1, 0.1):
	fixations.append(run_fixation(n_runs, af, n_pop))
plt.violinplot(fixations)
plt.title('Fixation time (for any allele) vs AF')
labels=[f'{i:.2f}' for i in np.arange(0, 1.1, 0.1)]
plt.xticks(ticks=np.arange(12), labels=['']+labels)
plt.xlabel('Allele frequency')
plt.ylabel('Fixation time')
plt.yscale('log')
plt.savefig('fixation_v_af_5.png')
plt.show()
