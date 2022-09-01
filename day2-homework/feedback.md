Nice work on this assignment! Your code (and Mike's code) is documented and commented well.

I also really like the level of thought you've put into matching SNPs between databases. This is something you'll have to deal with if you ever work with variant data - what exactly makes two things the same SNP, especially when one SNP can have multiple reference alleles? One way to reformat your dictionary to account for this could be to make the dbSNP key `(chrom, pos, ref, alt)`, and add in each alternative allele as a separate entry pointing to the same rsID.
