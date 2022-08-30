#!/usr/bin/env python
# Yein Christina Park
# Updated 08/30/2022
# Analyze gene BED file 

import sys
from bed_parser import parse_bed 

def get_median(bed, col=9):
  '''
  Calculate median of column specified in bed lines

  Args:
    bed (list): output of parse_bed; should be bed file contents where every line is split into fields
    col (int): Default 9 (blockCount). Index (starting from 0) of column of bed file to analyze for median 
  Returns:
    median (float): Median of column
  '''

  # Check inputs
  field_types = [str, int, int, str, float, str, int, int, list, int, list, list] 
  if len(bed[0]) <= col:
    # Too short
    print('Bed file does not have the column specified. Cannot analyze median.', file=sys.stderr)
    return 
  if field_types[col] not in [float, int]:
    # Not numbers
    print('Column specified does not contain numbers. Cannot analyze median.', file=sys.stderr)
    return 

  # to get median, get all values, sort, and get middle value 
  vals = sorted([b[col] for b in bed])

  if len(vals) % 2 == 0:
    # if even number of entries, it's len/2 and len/2-1 averaged together
    idx = len(vals)/2 # should be whole int b/c even 
    median = (vals[idx]+vals[idx-1])/2. # make sure float 
  else:
    # if odd number of entries, it's len/2 rounded up, then -1 for indexing
    idx = round(len(vals)/2) - 1
    median = vals[idx]

  print('Median number of values in column {} is {}'.format(col, median))
  return median 

if __name__ == "__main__":
  fname = sys.argv[1]

  bed = parse_bed(fname)
  try:
    # User can choose to specify column
    median = get_median(bed, int(sys.argv[2]))
  except:
    median = get_median(bed)