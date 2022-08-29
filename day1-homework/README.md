# QBB2022 - Day 1 - Homework Exercises Submission

## Exercise 1
- Running the command `source exercise1.sh ~/data/vcf_files/random_snippet.vcf` I see these errors:
```
Considering  A
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  C
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  G
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
Considering  T
awk: illegal field $(), name "nuc"
 input record number 21, file /Users/cmdb/data/vcf_files/random_snippet.vcf
 source line number 1
```
I decided to google `awk: illegal field $()`. Stack overflow told me that I needed to define variables outside awk with a `-v` flag or define it after awk. So I can change line 8 in the `exercise1.sh` file to define `nuc`.

I also had to get rid of the dollar sign in front of nuc in the awk string because I got another error message (`illegal field $(C), name "nuc"`)

This was my output from the script:
```
Considering  A
 354 C
1315 G
 358 T
Considering  C
 484 A
 384 G
2113 T
Considering  G
2041 A
 405 C
 485 T
Considering  T
 358 A
1317 C
 386 G
```
 - I'm not sure whether these make sense... A and G are most associated with each other, and C and T are most associated with each other. THis makes sense because chemically, A and G are purines and C and T are pyrimidines.


