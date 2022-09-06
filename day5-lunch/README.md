#Day 5 Lunch: Linear Regression

## Exercise 1
```
sort -k 5,5 -k 6,6 -t ',' aau1043_dnm.csv | cut -f 5,6 -d ',' | uniq -c > counts.txt

grep "mother" counts.txt | cut -f 1 -d , > mother.txt
grep "father" counts.txt | cut -f 1 -d , > father.txt

echo "# Proband_id father mother" > n_mutations.txt
join -1 2 -2 2 father.txt mother.txt >> n_mutations.txt

# Now do number 3
echo "# proband_ID father_age mother_age n_father n_mother" > final_data.txt
join <(sed 's/,/ /g' aau1043_parental_age.csv | sort -k 1,1) n_mutations.txt >> final_data.txt 
```

## Exercise 2
6. The relationship is significant because the t value is around 10. 22.8\% of the variation in number of maternal mutations can be explained by the change in the maternal age. The p value is smaller than 0.001. The slope is 0.4.
7. The relationship is even more significant, with t around 25. R-squared is 61.9\%. The p value is again smaller than 0.001. The slope is 1.4. This is the size of the relationship. 
8. The number of maternally vs paternally inherited genes seem to be significantly different, according to the t test for independence. The p value is like super small (like $10^{264}$)
10. 78 mutations predicted. Looking at the graph, this makes sense.

