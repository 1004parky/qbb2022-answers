#!/usr/bin/env python3

import sys
from vcfParser import parse_vcf

# Usage: python label_records.py vcf_unlabeled vcf_labeled [0 or 1]

def annotate(unlabeled, labels):
  '''
  Annotate one variant dataset with the IDs from another variant dataset

  Args:
    unlabeled (list): Parsed output from parse_vcf, should contain metadata and data from vcf file. This is the unlabeled dataset
    labels (list): Parsed output from parse_vcf, should contain metadata and data from vcf file. Will use IDs from this dataset
  Returns:
    labeled (list): Edited version of `unlabeled` with new labels from `labels` dataset
  '''
  ### Extract the pos:id info from datalines of labels dataset
  # Data line format (required entries): 
  # CHROM | POS | ID | REF | ALT | QUAL | FILTER | INFO | (other genotype fields)

  print('Using CHROM, POS, and REF, and ALT to match IDs')
  # alt can be a comma-separated list. the alt in unlabeled should be one of the alt's from the labels
  # Will not use alt in dict key but will make it a value as well so that
  # during the replace id part of the code I can check 

  reading_data = False
  id_dict = {}
  for d in labels:
    if d[0] == 'CHROM': continue # skip header line
    # use chrom, pos, ref
    key = (d[0], d[1], d[3])
    if key in id_dict and id_dict[key] != (d[4], d[2]):
      # if pos key exists, but maps to different ID, it means same ref, different alts
      # Keep the one with more alts; this is arbitrary
      if d[4].count(',') < id_dict[key][0].count(','):
        # Old line has more alts, ignore, otherwise will overwrite
        continue
    id_dict[key] = (d[4], d[2]) # ALT, ID

  ### Replace IDs in unlabeled based on id_dict -- check ALTs here
  # Track number of records without corresponding ID
  orphans = 0 
  for record in unlabeled:
    if record[0] == 'CHROM': continue # skip header line
    try:
      # replace ID based on (CHROM, POS, REF)
      match = id_dict[(record[0], record[1], record[3])]
      if record[4] in match[0].split(','):
        # if record ALT is one of ALTs from labels
        # Assumes that the unlabeled ALTs are only ever a single allele
        record[2] = match[1]
      else: raise Exception
    except:
      # that position doesn't exist
      orphans += 1

  print(f'{orphans} records did not have matching IDs in second file.')
  return unlabeled # It's actually labeled now  

if __name__ == "__main__":
  unlabeled = sys.argv[1]
  labeled = sys.argv[2]

  vcf_unlabeled = parse_vcf(unlabeled)
  vcf_labeled = parse_vcf(labeled)

  annotate(vcf_unlabeled, vcf_labeled)
    

