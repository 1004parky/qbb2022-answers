meta=/Users/cmdb/data/metadata_and_txt_files/integrated_call_samples.panel
vec=plink.eigenvec

grep -v '^sample' $meta | sort -k 1 > sorted_integrated_call_samples.panel

cut -d ' ' -f 2- $vec > sorted.eigenvec

join -1 1 -2 1 sorted_integrated_call_samples.panel sorted.eigenvec > eigenvec_metadata.txt


