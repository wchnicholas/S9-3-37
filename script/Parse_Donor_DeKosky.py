#!/usr/bin/python
import os
import sys
import glob
import operator
from Bio import pairwise2
from itertools import imap
from collections import Counter

def hamming(str1, str2):
    assert len(str1) == len(str2)
    return sum(imap(operator.ne, str1, str2))

def translation(seq):
  dnamap = {"TTT":"F", "TTC":"F", "TTA":"L", "TTG":"L",
    "TCT":"S", "TCC":"S", "TCA":"S", "TCG":"S",
    "TAT":"Y", "TAC":"Y", "TAA":"_", "TAG":"_",
    "TGT":"C", "TGC":"C", "TGA":"_", "TGG":"W",
    "CTT":"L", "CTC":"L", "CTA":"L", "CTG":"L",
    "CCT":"P", "CCC":"P", "CCA":"P", "CCG":"P",
    "CAT":"H", "CAC":"H", "CAA":"Q", "CAG":"Q",
    "CGT":"R", "CGC":"R", "CGA":"R", "CGG":"R",
    "ATT":"I", "ATC":"I", "ATA":"I", "ATG":"M",
    "ACT":"T", "ACC":"T", "ACA":"T", "ACG":"T",
    "AAT":"N", "AAC":"N", "AAA":"K", "AAG":"K",
    "AGT":"S", "AGC":"S", "AGA":"R", "AGG":"R",
    "GTT":"V", "GTC":"V", "GTA":"V", "GTG":"V",
    "GCT":"A", "GCC":"A", "GCA":"A", "GCG":"A",
    "GAT":"D", "GAC":"D", "GAA":"E", "GAG":"E",
    "GGT":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
  pep = []
  i = 0
  while i < len(seq):
    codon = seq[i:i+3]
    aa = dnamap[codon]
    pep.append(aa)
    i = i + 3
  pep = ''.join(pep)
  return pep

def search_motif(CDRH3, motif, max_mismatch):
  for n in range(0, len(CDRH3)-len(motif)+1):
    CDRH3_motif = CDRH3[n:n+len(motif)]
    if hamming(motif, CDRH3_motif) <= max_mismatch:
      if motif=='ILTG' and CDRH3_motif[1]=='L':
        return 'yes', CDRH3_motif
      if motif=='LRYFDWL' and CDRH3_motif[0]+CDRH3_motif[2:4]+CDRH3_motif[5::]=='LYFWL':
        return 'yes', CDRH3_motif
  return 'no', '-'

def parse_donor_file(filename, donorID, outfile_HD39, outfile_Dgene):
  infile = open(filename, 'r')
  Dgene_dict = {}
  HD39_count = 0
  ILTG_count = 0
  LRYFDWL_count = 0
  Total_count   = 0
  Dgene_ref = 'GTATTACGATATTTTGACTGGTTATTATAAC'
  for line in infile.xreadlines():
    if line[0:10] == 'Read Count': continue
    line  = line.rsplit("\t")
    count     = int(line[0])
    CDRH3_dna = line[1].upper()
    CDRH3     = translation(CDRH3_dna)[3::]
    CDRH3_len = len(CDRH3)
    Vgene     = line[3]
    Dgene     = line[5]
    Total_count += count
    assert('_' not in CDRH3)
    if 'HD3-9' in Dgene:
      HD39_count += count
      ILTG, ILTG_motif = search_motif(CDRH3, 'ILTG', 1)
      LRYFDWL, LRYFDWL_motif = search_motif(CDRH3, 'LRYFDWL', 2)
      if ILTG=='yes': ILTG_count += count
      if LRYFDWL=='yes': LRYFDWL_count += count
      outfile_HD39.write("\t".join(map(str,['Donor '+donorID, Vgene, Dgene, CDRH3_len, ILTG, LRYFDWL, CDRH3, count]))+"\n")
  outfile_Dgene.write("\t".join(map(str,['Donor '+donorID, Total_count, HD39_count, ILTG_count, LRYFDWL_count]))+"\n")
  infile.close()
  return Dgene_dict

def main():
  filenames = glob.glob('data/Donor*.tsv')
  outfile_HD39  = 'result/HD39_Donor_summary.tsv'
  outfile_Dgene = 'result/Dgene_Donor_summary.tsv'
  outfile_HD39  = open(outfile_HD39, 'w')
  outfile_Dgene = open(outfile_Dgene, 'w')
  outfile_HD39.write("\t".join(['donorID', 'Vgene', 'Dgene', 'CDRH3_len', 'ILTG', 'LRYFDWL', 'CDRH3', 'count'])+"\n")
  outfile_Dgene.write("\t".join(map(str,['Subject', 'Total_count', 'HD39_count', 'ILTG_count', 'LRYFDWL_count']))+"\n")
  for filename in filenames:
    donorID = filename.rsplit('.')[0].rsplit('Donor')[1]
    print 'Analyzing donor %s' % donorID
    Dgene_dict = parse_donor_file(filename, donorID, outfile_HD39, outfile_Dgene)
  outfile_HD39.close()
  outfile_Dgene.close()
    
if __name__ == "__main__":
  main()
