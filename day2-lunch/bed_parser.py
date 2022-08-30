#!/usr/bin/env python3
# Yein Christina Park
# Updated 08/30/2022
# Parse bed files, return lines as lists of fields

import sys

def parse_bed(fname):
  '''
  parse bed3-9 or bed12 files

  Args:
    fname (str): name of bed file 
  Returns:
    bed (list): list of lists (field-separated) of correctly-formatted lines from fname
  '''

  # Example line of bed12 format 
  # chr21   5086739 5087232 ENST00000701545.1       0       +       5086739 5086739 0,100,0 1       493,    0,

  # Check inputs
  try:
    f = open(fname, 'r')
  except:
    raise FileNotFoundError("That file doesn’t appear to exist")

  bed = []
  field_types = [str, int, int, str, float, str, int, int, list, int, list, list] 

  # track # malformed lines
  n_malformed = 0

  for line in f: 
    if line.startswith('#'):
      # skip comments 
      continue
    fields = line.rstrip().split()
    fieldN = len(fields)
    if fieldN < 3 or fieldN in [10, 11] or fieldN > 12:
      # line must have 3-9 or 12 entries
      n_malformed += 1
      continue
    try:
      # parse inputs, verify types
      for j in range(min(len(field_types), len(fields))):
        if j in [8, 10, 11]:
          # list entries (9th, 11th, 12th) 
          fields[j] = field_types[j](map(int, fields[j].strip(',').split(',')))
          if j == 8 and (len(fields[j]) != 3): 
            # 9th entry should be 3 integers long
            raise Exception 
          if j in [10, 11] and (len(fields[j]) != fields[9]): 
            # 11th and 12th entries need to be same length as specified by 10th entry
            raise Exception 
        else:
          # all other entries
          fields[j] = field_types[j](fields[j])
      bed.append(fields)
    except:
      n_malformed += 1
  f.close()

  if n_malformed > 0: 
    print('{} lines were malformed and were not processed'.format(n_malformed), file=sys.stderr)
  
  return bed

if __name__ == "__main__":
  fname = sys.argv[1]
  bed = parse_bed(fname)
