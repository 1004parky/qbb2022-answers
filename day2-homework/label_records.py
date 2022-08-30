#!/usr/bin/env python3

import sys
from vcfParser import parse_vcf

# Usage: python label_records.py vcf_unlabeled vcf_labeled [0 or 1]

def annotate(unlabeled, labels, robust=False):
  '''
  Annotate one variant dataset with the IDs from another variant dataset

  Args:
    unlabeled (list): Parsed output from parse_vcf, should contain metadata and data from vcf file. This is the unlabeled dataset
    labels (list): Parsed output from parse_vcf, should contain metadata and data from vcf file. Will use IDs from this dataset
    robust (bool): Default False. If True, will map IDs based on (position, reference, alternate) tuple rather than just position. 
                    Any overwrites (non-unique mappings) will stop the program.
                   If False, will map IDs based only on position; any duplicate mappings will be ignored (only the first ID will be kept)
  Returns:
    labeled (list): Edited version of `unlabeled` with new labels from `labels` dataset
  '''
  ### Extract the pos:id info from datalines of labels dataset
  # Data line format (required entries): 
  # CHROM | POS | ID | REF | ALT | QUAL | FILTER | INFO | (other genotype fields)

  if robust:
    print('Using POS, REF, and ALT to match IDs')
  else:
    print('Using just POS to match IDs')

  reading_data = False
  id_dict = {}
  for d in labels:
    if reading_data:
      if robust:
        # use pos, ref, alt
        if (d[1], d[3], d[4]) in id_dict and id_dict[(d[1], d[3], d[4])] != d[2]:
          # if pos key exists, but maps to different ID, print warning
          raise Exception('Labeled dataset contained duplicate (POS, REF, ALT) value with different ID values.')
        id_dict[(d[1], d[3], d[4])] = d[2]
      else: # not robust
        if d[1] in id_dict: 
          # if pos key exists, ignore 
          continue 
        id_dict[d[1]] = d[2]
    elif d[0] == 'CHROM': 
      # Line with column names immediately precedes data rows 
      reading_data = True 

  ### Replace IDs in unlabeled based on id_dict
  # Track number of records without corresponding ID
  orphans = 0 
  for record in unlabeled:
    try:
      # replace ID based on position or (POS, REF, ALT)
      if robust:
        record[2] = id_dict[(record[1], record[3], record[4])]
      else:
        record[2] = id_dict[record[1]]
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

  try:
    # User specifies robust or not 
    annotate(vcf_unlabeled, vcf_labeled, bool(sys.argv[3]))
  except:
    annotate(vcf_unlabeled, vcf_labeled)
    

