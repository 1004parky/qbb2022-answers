#!/usr/bin/env python

#USAGE: python scriptname.py KRAKEN_sample_input_file.kraken sample_name
#EXAMPLE: python make_krona_compatible.py KRAKEN/SRR492183.kraken SRR492183

import sys
import os

for file in os.listdir(sys.argv[1]+'/'):
    if os.path.isfile(os.path.join(sys.argv[1]+'/', file)):
        if file.endswith('.kraken'):
            fname = file.split('.')[0] + '_krona.txt'
            out = open(os.path.join(sys.argv[1]+'/', fname), 'w')
            with open(os.path.join(sys.argv[1]+'/', file), 'r') as f:
                for line in f:
                    fields = line.strip('\r\n').split(';')
                    out.write("\t".join(fields[1:]) + "\n")