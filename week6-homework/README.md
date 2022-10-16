### Week 6

For dCTCF:
- 92\% of reads are valid
- The majority of invalid 3C pairs are dangling end pairs. That means "unligated fragments (both reads mapped on the same restriction fragment)"

For ddCTCF:
- 88\% of reads are valid
- The majority of invalid 3C pairs are also dangling end pairs

#### Part 2
- I don't think I can see the highlighted difference. I think we are using mm10 instead of mm9. 
- More sequencing depth gives you better resolution and higher intensities. With insufficient depth, you might miss some interactions. 
- The highlighted signal... represents the CTCF binding sites. 

- Note: for the insulation scores part, the instructions said to plot for bins 54878 to 54951, which are only valid bins for the 40K data. However, we were also told over slack to use the 6400 data for this part. Also, we only have 40K data for dCTCF, not ddCTCF. The region specified (chr15:10400000-13400000) corresponds to other bins for the 6400 data. So I recalculated the bins for the "full dataset" part and used 6400 data. 