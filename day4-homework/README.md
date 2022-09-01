# QBB2022 – Day 4 Homework: Visualizing Simulation Results and Power

## A
The `probs` line:
- Take a list of numbers going from 0.55 to 1.00 (inclusive) incrementing by 0.05. Then round tall numbers in this array to two decimal places.. (I'm not sure why the around is needed because doesn't arange already return in 0.05 increments?). Then, the list slicing reverses the array.
Note, the `prob_heads` and `n_toss` args are now obsolete so got rid of them.

## D
The biological phenomenon of interest is transmission distortion, where some alleles are disproportionately passed down to the next generation (rather than an equal proportion). In the study they were analyzing this phenomenon on a new sperm dataset.

The simulation experiments are the same, just that the variables represent other concepts. P(head) was transmission rates, and the number of tosses were the number of sperm. We used 100 iterations while they used 1000 iterations, but that's a small difference. Both simulations use a binomial test because in both cases, we have two possible outcomes. heads or tails, transmitted or not.

