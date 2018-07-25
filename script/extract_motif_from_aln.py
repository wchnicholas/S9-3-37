#!/usr/bin/python
import os
import sys
import glob
import scipy as sc
import numpy as np
from math import log
from Bio import SeqIO
from collections import Counter

def extract_resi_subtypes_aln(infile, outfile):
  seq_dict = {}
  handle  = open(infile, "rU")
  outfile = open(outfile, 'w')
  for record in SeqIO.parse(handle, "fasta"):
    ID  = str(record.id)
    seq = str(record.seq)
    motif = seq[33]+seq[42:46]+seq[53:56]+seq[348]+seq[350:354]+seq[378]+seq[380]+seq[413:417]+ \
            seq[431]+seq[433:435]+seq[436:439]+seq[440:442]+seq[443:446]+seq[447:450]+seq[451:453]
    seq_dict[ID] = motif
    outfile.write(ID.replace('(',' (').replace('_',' ')+"\t"+"\t".join(list(motif))+"\n")
  handle.close()
  outfile.close()
  return seq_dict

def entropy(labels):
  count_dict = Counter(labels)
  H = 0
  for label in count_dict.keys():
    freq = float(count_dict[label])/float(sum(count_dict.values()))
    H += -freq*log(freq, 2)
  return H

def reading_resi_info(filename):
  resi_info_dict = {}
  resi_list = []
  infile = open(filename, 'r')
  for line in infile.xreadlines():
    if 'chain' in line: continue
    line = line.rstrip().rsplit("\t")
    resi_list.append(line[0]+'-'+line[1])
    resi_info_dict[line[0]+'-'+line[1]] = line[2]
  infile.close()
  return resi_info_dict, resi_list

def compute_resi_entropy(seq_dict, resi_info_dict, resi_list, outfile):
  outfile = open(outfile,'w')
  outfile.write("\t".join(['resi','entropy','class'])+"\n")
  for n in range(len(resi_list)):
    resi = resi_list[n]
    aas  = []
    for ID in seq_dict.keys():
      aas.append(seq_dict[ID][n])
    outfile.write("\t".join(map(str,[resi, entropy(aas), resi_info_dict[resi]]))+"\n")
  outfile.close()

def main():
  outfile = 'result/Epitope_seq_entropy.tsv'
  file_all_aln = 'Fasta/HAdiffSubtypes.aln'
  file_all_out = 'Fasta/Motif.aln'
  resi_info_dict, resi_list = reading_resi_info('doc/Epitopes.tsv')
  seq_dict     = extract_resi_subtypes_aln(file_all_aln, file_all_out)
  compute_resi_entropy(seq_dict, resi_info_dict, resi_list, outfile)
  
if __name__ == "__main__":
  main()
