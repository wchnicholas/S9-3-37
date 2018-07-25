#!/usr/bin/python
import os
import sys
import glob
import scipy as sc
import numpy as np
from math import log
from Bio import SeqIO
from collections import Counter

def extract_resi_subtypes_aln(infile, file_all_out_38, file_all_out_50):
  print "writing: %s" % file_all_out_38
  print "writing: %s" % file_all_out_50
  handle  = open(infile, "rU")
  outfile_38 = open(file_all_out_38, 'w')
  outfile_50 = open(file_all_out_50, 'w')
  count = 0
  for record in SeqIO.parse(handle, "fasta"):
    count += 1
    ID  = str(record.id)
    seq = str(record.seq)
    resi50 = seq[484] #HA2 resi 50
    resi38 = seq[83:86] #HA1 resi 38-40
    subtype = ID.rsplit('|')[-2]
    if '(' in subtype and ')' in subtype: subtype = subtype.rsplit('(')[1].rsplit(')')[-2]
    else: subtype = subtype.rsplit('_')[-2]
    outfile_38.write(ID+"\t"+subtype+"\t"+resi38+"\n")
    outfile_50.write(ID+"\t"+subtype+"\t"+resi50+"\n")
  handle.close()
  outfile_38.close()
  outfile_50.close()

def main():
  file_all_aln = 'Fasta/Natural_All_Subtypes.aln'
  file_all_out_38 = 'result/Resi38.tsv'
  file_all_out_50 = 'result/Resi50.tsv'
  extract_resi_subtypes_aln(file_all_aln, file_all_out_38, file_all_out_50)
  
if __name__ == "__main__":
  main()
