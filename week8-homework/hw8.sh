# Part 1
regions=("chr11:1900000-2800000 chr14:100700000-100990000 chr15:23600000-25900000 chr20:58800000-58912000") 

for r in ${regions}; do 
	chr=${r%:*}
	echo ${chr}
	medaka_variant -i methylation.bam -f hg38.fa -r ${r} -o ${chr} -p ${chr}_phased.vcf 
done

# Part 2
regions=("chr11:1900000:2800000 chr14:100700000:100990000 chr15:23600000:25900000 chr20:58800000:58912000") 
chroms=""

for r in ${regions}; do 
	chr=${r%:*:*}
	echo ${chr}
	chroms="${chroms} ${chr}"
	whatshap haplotag -o ${chr}/${chr}_phased.bam -r hg38.fa --regions ${r} --output-haplotag-list ${chr}/${chr}_haplotags.txt ${chr}/round_0_hap_mixed_phased.vcf.gz methylation.bam
done

# Step 3
for chr in ${chroms}; do 
	echo ${chr}
	whatshap split --output-h1 ${chr}/${chr}_h1.bam --output-h2 ${chr}/${chr}_h2.bam ${chr}/${chr}_phased.bam ${chr}/${chr}_haplotags.txt
done

# Concatenate bam files by haplotype
h1s=""
h2s=""
for chr in ${chroms}; do
	echo ${chr}
	h1s="${h1s} ${chr}/${chr}_h1.bam"
	h2s="${h2s} ${chr}/${chr}_h2.bam"
done

echo ${h1s}
echo ${h2s}

samtools cat -o haplotype1.bam ${h1s}
samtools cat -o haplotype2.bam ${h2s}

samtools index haplotype1.bam 
samtools index haplotype2.bam 


conda deactivate
conda create -n igv gradle openjdk=11 -y
conda activate igv
git clone https://github.com/igvteam/igv.git

cd igv
./gradlew createDist
cd ../


ln -s ${PWD}/igv/build/IGV-dist/igv.sh ./

source igv.sh