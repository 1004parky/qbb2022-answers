# Coding Bootcamp 2022
# Applied Python Exercise 7
# Yein Christina Park
# https://kweav.github.io/prepwork_revamp/introduction.html

import sys 

'''
  Reproduces bash 'tail' command. 
  Run from commandline:
  python PARK_tail.py path_to_file [num_lines]

  INPUTS:
  path_to_file (str, required)         : file name to read out from
  num_lines (int, optional, default 10): number of lines to print from end of file
'''

fname = sys.argv[1]
try:
  nlines = int(sys.argv[2])
except:
  nlines = 10 # default value

# Check user inputs
if nlines < 0:
  raise ValueError('Number of lines cannot be negative')
  
try:
  with open(fname) as f:
    lines = f.read().splitlines() # get all lines, without \n
except:
  raise FileNotFoundError('File cannot be read. Make sure it exists')

if nlines != 0: 
  # With this syntax, edgecase when nlines == 0; should print no lines
  print('\n'.join(lines[-nlines:])) # print lines starting with nlines from the end
