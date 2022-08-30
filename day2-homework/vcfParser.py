#!/usr/bin/env python3

import sys

def parse_vcf(fname):
  '''
  Parse vcf files, return data as list of fields
  
  Args:
    fname (str): Name of file 
  Returns:
    vcf (list): data from file as a list of lines, each of which are a list of fields
  '''

  vcf = []
  info_description = {}
  info_type = {}
  format_description = {}
  type_map = {
    "Float": float,
    "Integer": int,
    "String": str
    }
  malformed = 0

  # Check input
  try:
    f = open(fname)
  except:
    raise FileNotFoundError(f"{fname} does not appear to exist", file=sys.stderr)

  for line in f:
      if line.startswith("#"):
        try:
          # Parse header lines; contain valuable information
          if line.startswith("##FORMAT"):
            fields = line.split("=<")[1].rstrip(">\r\n") + ","
            i = 0
            start = 0
            in_string = False
            while i < len(fields):
              if fields[i] == "," and not in_string:
                if fields[start:i].count("=") == 1:
                  name, value = fields[start:i].split('=')
                  if name == "ID":
                    ID = value
                  elif name == "Description":
                    desc = value
                start = i + 1
              elif fields[i] == '"':
                in_string = not in_string
              i += 1
            format_description[ID] = desc.strip('"')
          elif line.startswith("##INFO"):
            # parse info info line, associate description with ID
            fields = line.split("=<")[1].rstrip(">\r\n") + ","
            i = 0
            start = 0
            in_string = False
            while i < len(fields):
              if fields[i] == "," and not in_string:
                if fields[start:i].count("=") == 1:
                  name, value = fields[start:i].split('=')
                  if name == "ID":
                    ID = value
                  elif name == "Description":
                    desc = value  
                  elif name == "Type":
                    Type = value  
                start = i + 1
              elif fields[i] == '"':
                in_string = not in_string
              i += 1
            info_description[ID] = desc.strip('"')
            info_type[ID] = Type
          elif line.startswith('#CHROM'):
            # parse column line. 
            fields = line.lstrip("#").rstrip().split("\t")
            vcf.append(fields)
        except:
          raise RuntimeError("Malformed header")
      else:
        # Data lines
        # 8 fixed fields
        # CHROM | POS | ID | REF | ALT | QUAL | FILTER | INFO | (other genotype fields)
        # all rows must have the same columns
        try:
          fields = line.rstrip().split("\t")
          fields[1] = int(fields[1]) # pos
          if fields[5] != ".":
            fields[5] = float(fields[5]) # qual 
          info = {}
          for entry in fields[7].split(";"): # info 
            # for every data value in info 
            temp = entry.split("=")
            if len(temp) == 1:
              info[temp[0]] = None
            else:
              name, value = temp
              Type = info_type[name] # capitalize Type since type is a keyword..
              info[name] = type_map[Type](value)
          fields[7] = info # info is dict
          if len(fields) > 8: # format column precedes any genotype data columns
            fields[8] = fields[8].split(":")
            if len(fields[8]) > 1:
                for i in range(9, len(fields)):
                  # All the genotype data
                  fields[i] = fields[i].split(':')
            else:
              # If only one genotype column, just store it as the string, not list 
              fields[8] = fields[8][0]
          vcf.append(fields)
        except:
          # Keep track of how many malformed lines
          malformed += 1

  # after parsing file, set 8th element of 1st parsed row as info_description...   
  vcf[0][7] = info_description
  if len(vcf[0]) > 8:
    vcf[0][8] = format_description
  if malformed > 0:
    # report number of malformed lines
    print(f"There were {malformed} malformed entries", file=sys.stderr)
  return vcf

if __name__ == "__main__":
  fname = sys.argv[1]
  vcf = parse_vcf(fname)
  for i in range(10):
    # print just the first 10 rows of output, because vcf files can be giant!
    print(vcf[i])
