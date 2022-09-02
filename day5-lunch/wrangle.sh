sort -k 5,5 -k 6,6 -t ',' aau1043_dnm.csv | cut -f 5,6 -d ',' | uniq -c > counts.txt

grep "mother" counts.txt | cut -f 1 -d , > mother.txt
grep "father" counts.txt | cut -f 1 -d , > father.txt

echo "# Proband_id father mother" > n_mutations.txt
join -1 2 -2 2 father.txt mother.txt >> n_mutations.txt

# Now do number 3
echo "# proband_ID father_age mother_age n_father n_mother" > final_data.txt
join <(sed 's/,/ /g' aau1043_parental_age.csv | sort -k 1,1) n_mutations.txt >> final_data.txt 

