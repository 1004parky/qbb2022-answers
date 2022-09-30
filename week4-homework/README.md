### Homework 4

2. Plink PCA: Included freq flag to get allele frequency data for 3. All plots are plotted in python, code is in hw4.py
```
plink --vcf gwas_data/genotypes.vcf --pca 10 --freq 
```
4. First combine phenotypes:
```
cut -f 3 GS451_IC50.txt > GS451_pheno_IC50.txt
paste CB1908_IC50.txt GS451_pheno_IC50.txt > combined_IC50.txt
plink --vcf gwas_data/genotypes.vcf --assoc --pheno gwas_data/combined_IC50.txt --all-pheno --linear --allow-no-sex --covar plink.eigenvec --hide-covar
```
7. I printed the most significant SNP ids from each phenotype:
```
Most significant association SNP ID for plink.GS451_IC50.assoc.linear: rs7257475
Most significant association SNP ID for plink.CB1908_IC50.assoc.linear: rs10876043
```
Then I looked up these IDs. For the GS451, I found that that SNP is in human gene ZNF826, which is a Zinc finger protein. For CB1908, I found gene DIP2B. May participate in DNA methylation.

I looked in the VCF file and found no mention of hg18. The listed date was also in 2021, when hg18 would not have been the most recent build. So I'm not sure where one would find this information.