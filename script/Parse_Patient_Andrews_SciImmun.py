#!/usr/bin/python
import os
import sys
import glob
import operator
from itertools import imap
from collections import Counter

def hamming(str1, str2):
    assert len(str1) == len(str2)
    return sum(imap(operator.ne, str1, str2))

def parse_Andrews_patient_file(filename):
  infile = open(filename, 'r')
  Dgene_dict = {}
  for line in infile.xreadlines():
    if line[0:3] == 'mAb': continue
    line  = line.rsplit("\t")
    name  = line[3]
    Vgene = line[4].rsplit(' ')[1].replace('IG','')
    Dgene = line[6].rsplit(' ')[1].replace('IG','')
    CDRH3 = line[8]
    CDRH3_len = len(CDRH3)
    assert(len(CDRH3)==int(CDRH3_len))
    if Dgene_dict.has_key(name):
      print name
      print "Duplicate name!!"
      sys.exit()
    Dgene_dict[name] = {'name':name, 'Dgene':Dgene, 'Vgene':Vgene,
                        'CDRH3':CDRH3, 'CDRH3_len':CDRH3_len}
  infile.close()
  return Dgene_dict

def search_motif(CDRH3, motif, max_mismatch):
  for n in range(0, len(CDRH3)-len(motif)+1):
    CDRH3_motif = CDRH3[n:n+len(motif)]
    if hamming(motif, CDRH3_motif) <= max_mismatch:
      if motif=='ILTG' and CDRH3_motif[1]=='L':
        return 'yes', CDRH3_motif
      if motif=='LRYFDWL' and CDRH3_motif[0]+CDRH3_motif[2:4]+CDRH3_motif[5::]=='LYFWL':
        return 'yes', CDRH3_motif
  return 'no', '-'

def analyze_Dgene(Dgene_dict, patientID, outfile_HD39, outfile_Dgene):
  HD39_count = 0
  ILTG_count = 0
  LRYFDWL_count = 0
  Total_count = 0
  print "Analyzing patient: %s" % patientID
  for name in Dgene_dict.keys():
    if patientID != '-'.join(name.rsplit('-')[0:2]): continue
    Total_count += 1
    Vgene = Dgene_dict[name]['Vgene']
    Dgene = Dgene_dict[name]['Dgene']
    CDRH3 = Dgene_dict[name]['CDRH3'][2::]
    CDRH3_len = str(int(Dgene_dict[name]['CDRH3_len'])-2)
    if 'HD3-9' in Dgene:
      HD39_count += 1
      ILTG, ILTG_motif = search_motif(CDRH3, 'ILTG', 1)
      LRYFDWL, LRYFDWL_motif = search_motif(CDRH3, 'LRYFDWL', 2)
      if ILTG=='yes': ILTG_count += 1
      if LRYFDWL=='yes': LRYFDWL_count += 1
      outfile_HD39.write("\t".join(['Subject '+str(int(patientID.rsplit('-')[1])), name,
                                    Vgene, Dgene, CDRH3_len, ILTG, LRYFDWL, CDRH3])+"\n")
  outfile_Dgene.write("\t".join(map(str,['Subject '+str(int(patientID.rsplit('-')[1])),
                                          Total_count, HD39_count, ILTG_count, LRYFDWL_count]))+"\n")

def main():
  filename = 'data/Andrews_SciImmun.tsv'
  outfile_HD39  = 'result/HD39_Andrews_SciImmun_Patient_summary.tsv'
  outfile_Dgene = 'result/Dgene_Andrews_SciImmun_Patient_summary.tsv'
  outfile_HD39  = open(outfile_HD39, 'w')
  outfile_Dgene = open(outfile_Dgene, 'w')
  outfile_HD39.write("\t".join(['patientID', 'name', 'Vgene', 'Dgene', 'CDRH3_len', 'ILTG', 'LRYFDWL', 'CDRH3'])+"\n")
  outfile_Dgene.write("\t".join(map(str,['Subject', 'Total_count', 'HD39_count', 'ILTG_count', 'LRYFDWL_count']))+"\n")
  Dgene_dict = parse_Andrews_patient_file(filename)
  patientIDs = list(set((['-'.join(ID.rsplit('-')[0:2]) for ID in Dgene_dict.keys()])))
  for patientID in sorted(patientIDs):
    analyze_Dgene(Dgene_dict, patientID, outfile_HD39, outfile_Dgene)
  outfile_HD39.close()
  outfile_Dgene.close()
    
    
if __name__ == "__main__":
  main()
