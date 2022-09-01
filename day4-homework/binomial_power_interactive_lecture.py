#!/usr/bin/env python
# Edited by Yein Christina Park 9/1/2022

import numpy
from scipy.stats import binomtest
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.multitest import multipletests

def simulate_coin_toss(n_tosses, prob_heads = 0.5, seed=None):
    '''
    Simulates a coin toss (fair or unfair depending on prob_heads)
    Input: n_tosses, an integer, number of coin tosses to simulate
           prob_heads, a float, the probability the coin toss will return heads; default is 0.5, meaning a fair coin
           seed, an integer, the random seed that will be used in the simulation; default is None
    Output: results_arr, an array of 1's and 0's with 1's representing heads and 0's representing tails
    Resources: https://numpy.org/doc/stable/reference/random/generated/numpy.random.choice.html
    '''
    if seed is not None:
        numpy.random.seed(seed)
    results_arr = numpy.random.choice([0,1], size=n_tosses, p = [1-prob_heads, prob_heads])
    return (results_arr)

def perform_hypothesis_test(n_heads, n_tosses):
    '''
    Performs a two-sided binomial test
    Input: n_heads, an integer, number of coin tosses that resulted in heads/success
           n_tosses, an integer, total number of coin tosses/trials
    Output: pval, a float reporting the final pvalue from the binomial test
    Resources: https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binomtest.html#scipy.stats.binomtest
    '''
    binom_result = binomtest(n_heads, n_tosses)
    pval = binom_result.pvalue
    return(pval)

def correct_pvalues(pvals):
    '''
    Will apply the bonferroni multiple hypothesis testing correction method to input pvalues
    Input: pvals, an array-like object containing uncorrected pvalues
    Output: corrected_pvalues[1], an array containing corrected pvalues
    Resources: https://www.statsmodels.org/dev/generated/statsmodels.stats.multitest.multipletests.html
    '''
    corrected_pvalues = multipletests(pvals, method='bonferroni')
    return(corrected_pvalues[1])

def interpret_pvalues(pvals):
    '''
    Will interpret or convert pvalues from floats to booleans (Trues or Falses) reporting whether or not you reject the null hypothesis
    True -- reject null Hypothesis
    False -- fail to reject null hypothesis
    Input: pvals, an array-like object containing pvalues (floats)
    Output: interpreted, an array containing booleans
    '''
    interpreted = numpy.array(pvals) < 0.05
    return (interpreted)

def compute_power(n_rejected_correctly, n_tests):
    '''
    Will compute the power, defined as the number of correctly rejected null hypothesis divided by the total number of tests (AKA the True Positive Rate or the probability of detecting something if it's there)
    Input: n_rejected_correctly, an integer, the total number of tests in which the null hypothesis was correctly rejected
           n_tests, an integer, the total number of hypothesis tests which were performed
    output: power, a float, the power
    '''
    power = n_rejected_correctly / n_tests
    return(power)

def run_experiment(n_iters = 100, seed = 389, correct_the_pvalues = False):
    '''
    Will run several coin toss experiments using combinations of P(head) and number of tosses
    as specified in the body of the function. 

    Input: n_iters, an integer, the number of iterations for each simulation. default is 100
           seed, an integer, the random seed that you will set for the whole simulation experiment. default is 389
           correct_the_pvalues, a boolean, whether or not to perform multiple hypothesis testing correction
    Output: power, a float, the power of the experiment
    '''
    numpy.random.seed(seed)

    # bunch of tosses and probs
    tosses = numpy.array([10, 50, 100, 250, 500, 1000])
    probs = numpy.around(numpy.arange(0.55, 1.05, 0.05), decimals=2)[::-1]

    powers = numpy.zeros((len(probs), len(tosses)))
    powers_corrected = numpy.zeros((len(probs), len(tosses)))

    for i, prob_heads in enumerate(probs):
        for j, n_toss in enumerate(tosses):
            # for each condition
            pvals = []
            for k in range(n_iters):
                # do experiment of n_toss coin tosses, n_iters times
                results_arr = simulate_coin_toss(n_toss, prob_heads = prob_heads)
                n_success = numpy.sum(results_arr)
                # calculate pval for each iteration
                pvals.append(perform_hypothesis_test(n_success, n_toss))

            pvals_corrected = correct_pvalues(pvals)

            # translate pvals to bool
            pvals_translated_to_bools = interpret_pvalues(pvals)
            powers[i][j] = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)
            
            pvals_translated_to_bools = interpret_pvalues(pvals_corrected)
            powers_corrected[i][j] = compute_power(numpy.sum(pvals_translated_to_bools), n_iters)

    # plot with and without correction 
    fig, ax = plt.subplots(ncols=2)
    sns.heatmap(powers, ax=ax[0], vmin=0, vmax=1, cmap='viridis', xticklabels=tosses, yticklabels=probs, linewidths=0.1)
    sns.heatmap(powers_corrected, ax=ax[1], vmin=0, vmax=1, cmap='viridis', xticklabels=tosses, yticklabels=probs, linewidths=0.1)
    
    for i in range(len(ax)):
        ax[i].set_ylabel('P(heads)')
        ax[i].set_xlabel('number of coin tosses')

    ax[0].set_title('With correction')
    ax[1].set_title('Without correction')

    fig.suptitle('Power of coin toss simulations')
    plt.tight_layout()
    fig.savefig('power_c.png')
    return powers, powers_corrected

run_experiment()