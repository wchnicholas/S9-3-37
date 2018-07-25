#!/usr/bin/python
import os
import sys
import json
import gzip
import glob
import operator
from itertools import imap
from collections import Counter

def hamming(str1, str2):
    assert len(str1) == len(str2)
    return sum(imap(operator.ne, str1, str2))

def read_filename(filename_list):
  filename_dict = {}
  infile = open(filename_list,'r')
  for line in infile.xreadlines():
    if 'sample' == line[0:6]: continue
    line = line.rstrip().rsplit("\t")
    sample   = line[0]
    filename = line[1]
    filename_dict[sample] = filename
  infile.close()
  return filename_dict

def search_motif(CDRH3, motif, max_mismatch):
  for n in range(0, len(CDRH3)-len(motif)+1):
    CDRH3_motif = CDRH3[n:n+len(motif)]
    if hamming(motif, CDRH3_motif) <= max_mismatch:
      if motif=='ILTG' and CDRH3_motif[1]=='L':
        return 'yes', CDRH3_motif
      if motif=='LRYFDWL' and CDRH3_motif[0]+CDRH3_motif[2:4]+CDRH3_motif[5::]=='LYFWL':
        return 'yes', CDRH3_motif
  return 'no', '-'

def analyze_OAS_Dgene(sample, filename, outfile_Dgene):
  HD39_count = 0
  ILTG_count = 0
  LRYFDWL_count = 0
  Total_count = 0
  print "Analyzing sample: %s" % sample
  infile = gzip.open(filename,'r')
  for line in infile.readlines():
    if 'Longitudinal' in line: continue
    Total_count += 1
    line  = json.dumps(line.rstrip().replace('"',''))
    CDRH3 = line.rsplit('cdr3: ')[1].rsplit(',')[0]
    CDRH3_len = len(CDRH3)-2
    ILTG, ILTG_motif = search_motif(CDRH3, 'ILTG', 1)
    LRYFDWL, LRYFDWL_motif = search_motif(CDRH3, 'LRYFDWL', 2)
    if ILTG=='yes': ILTG_count += 1
    if LRYFDWL=='yes': LRYFDWL_count += 1
  outfile_Dgene.write("\t".join(map(str,[sample, Total_count, ILTG_count, LRYFDWL_count]))+"\n")
  infile.close()

def main():
  filename_list = 'data/OAS_info.tsv'
  filename_dict = read_filename(filename_list)
  outfile_Dgene = 'result/Dgene_OAS_summary.tsv'
  outfile_Dgene = open(outfile_Dgene, 'w')
  outfile_Dgene.write("\t".join(map(str,['Subject', 'Total_count', 'ILTG_count', 'LRYFDWL_count']))+"\n")
  for sample in filename_dict.keys():
    filename = 'json/'+filename_dict[sample]
    analyze_OAS_Dgene(sample, filename, outfile_Dgene)
  outfile_Dgene.close()
    
if __name__ == "__main__":
  main()
