#!/usr/bin/env python3

import json
import argparse
import sys

parser = argparse.ArgumentParser(description="Convert chinese characters to peng'im with dictionary")
parser.add_argument("-i", "--input", type=argparse.FileType('r'), nargs='?', default=sys.stdin, action='store', help="File with chinese characters to be converted to peng'im")
parser.add_argument("-d", "--dict", type=str, action='store', help='JSON file with dictionary')
args=parser.parse_args()

# Read dictionary
dd_fh = open(args.dict, "r")
dd = json.load(dd_fh)
dd_fh.close()

# Process input

for line in args.input:
    out=[]
    line = line.rstrip()
    for char in line:
        if char in dd:
            if dd[char]['mn-t']:
                alts = "/".join(dd[char]['mn-t'])
                out.append(alts)
            else:
                out.append(char)
        else:
            out.append(char)
    print("".join(out))
    print("\n")
