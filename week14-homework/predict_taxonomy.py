import numpy as np

def parse_kraken(kraken):
	genus_dict = dict()
	species_dict = dict()
	with open(kraken, 'r') as f:
		for line in f:
			fields = line.split()
			name = fields[0] # this is identifier, e.g. NODE_2_length_556123_cov_2361.439230
			taxonomy = ' '.join(fields[1:]).split(';')
			try: 
				genus = taxonomy[8]
			except:
				# no genus info
				genus = '-'
			try: 
				species = taxonomy[9]
			except:
				spcies = '-'

			genus_dict[name] = genus 
			species_dict[name] = species

	return genus_dict, species_dict 

def count_ids(names, id_dict, idname=''):
	# Given list of sequence id's (names) and the corresponding taxonomic
	# classifications (id_dict), print out the percentages of those ids in
	# names. 
	print(f'{idname}categorization:')
	counts = dict()
	for n in names:
		category = id_dict[n]
		if category in counts:
			counts[category] += 1
		else:
			counts[category] = 1
	print('\tCategories identified in bin: {}'.format(counts))

kraken = 'metagenomics_data/step0_givendata/KRAKEN/assembly.kraken'

#bins_str = 'metagenomics_data/step3_givendata/bins/bin.{}.fa'
bins_str = 'metagenomics_data/step0_givendata/READS/bins.{}.fa'
n_bins = 6

genus_dict, species_dict = parse_kraken(kraken)



# Now, read in each bin fa
for i in range(n_bins):
	names = []
	with open(bins_str.format(i+1), 'r') as f:
		for line in f:
			if line.startswith('>'):
				names.append(line.strip('>\n'))
	count_ids(names, genus_dict, 'genus ')
	count_ids(names, species_dict, 'species ')
