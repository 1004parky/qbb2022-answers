from q1_2 import *

# Same as q1.2 with 15x coverage

random.seed(25) # set one seed 
genome = simulate(1e6, 15, 100)
plot_compare(genome, 15, 'q1.4', 'Simulated and theoretical 15x coverage of 1Mbp with 100 bp reads')