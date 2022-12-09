## Week 6 -- 10 points possible

1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 13 of 10 points possible

1. Given data question: What percentage of reads are valid interactions?

2. Given data question: What constitutes the majority of invalid 3C pairs?/What does it mean?

3. Script set up to (0.5 pts each)

  * read in data  
  * Filter data based on location  

4. Script set up to log transform the scores

5. Script set up to shift the data by subtracting minimum value

6. Script set up to convert sparse data into square matrix

7. Script set up to (0.33 pts each)

  * remove distance dependent signal
  * smooth
  * subtract

8. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for subset dataset (0.33 pts each ddCTCF/dCTCF/difference)

9. Turned in the plot of the 3 heatmaps (ddCTCF, dCTCF, and difference) for full dataset (0.33 pts each ddCTCF/dCTCF/difference)

10. Heatmap questions (0.33 pts each)

  * See the highlighted difference from the original figure?
  * impact of sequencing depth?
  * highlighted signal indicates?

Possible Bonus points:

1. Insulation script set up to (0.25 pts each)

  * read in data
  * filter data based on location
  * log transform the data
  * shift the data by subtracting minimum value

2. Insulation script set up to (0.5 pts each)

  * convert sparse data into square matrix
  * find the insulation score by taking mean of 5x5 squares of interactions around target

  I think the one yellow band in your plot is because of how you're iterating potentially? I used the following:
  ```
  starting_x = 10400000 + 200000 #first X coordinate should be 200K downstream of the upstream boundary of the heatmap, since you need to look 5 bins up and downstream to calculate the score
  for i in numpy.arange(5, N-4): #start at 5 since looking 5 below, and go until N-4 since looking 5 above
      scores.append(numpy.mean(mat[(i - 5):i, i:(i + 5)]))
      x_vals.append(starting_x)
      starting_x += 40000
  ```

3. Turned in the plot of the heatmap + insulation scores below (0.5 pts each panel)


Great code overall! wonderful variable names and I especially like the `axs[2].imshow((smooth_matrix(remove_dd_bg(d_mat))-smooth_matrix(remove_dd_bg(dd_mat))), cmap='seismic', norm=colors.CenteredNorm())`.

Surprised you didn't set a driver function that you called twice, once for the subset reads data and once for the full data, given that you repeat a lot of steps.
