#!/usr/bin/python
import os
import sys
import glob
import operator
from itertools import imap
from collections import Counter

def TsvWithHeader2Hash(file_tsv):
  H = {}
  infile = open(file_tsv,'r')
  countline = 0
  header = []
  for line in infile.xreadlines():
    countline += 1
    line = line.rstrip().rsplit("\t")
    if countline == 1: header = line; continue
    mut = line[0]
    H[mut] = {}
    for i in range(1,len(line)): H[mut][header[i]] = line[i]
  infile.close()
  return H

def format_HIV(OAS_dict, ID):
  HIV = {'Total_count': int(OAS_dict[ID+'_rep1']['Total_count'])+
                        int(OAS_dict[ID+'_rep2']['Total_count'])+
                        int(OAS_dict[ID+'_rep3']['Total_count']),
         'ILTG_count': int(OAS_dict[ID+'_rep1']['ILTG_count'])+
                       int(OAS_dict[ID+'_rep2']['ILTG_count'])+
                       int(OAS_dict[ID+'_rep3']['ILTG_count']),
         'LRYFDWL_count': int(OAS_dict[ID+'_rep1']['LRYFDWL_count'])+
                          int(OAS_dict[ID+'_rep2']['LRYFDWL_count'])+
                          int(OAS_dict[ID+'_rep3']['LRYFDWL_count'])}
  return HIV

def formatting(OAS_dict, HA_Joyce_dict, HA_Andrews_dict, HA_Andrews_STM_dict, HA_McCarthy_dict, HA_Pappas_dict, outfile):
  HIV_2012 = format_HIV(OAS_dict, 'HIV_2012')
  HIV_2014 = format_HIV(OAS_dict, 'HIV_2014')
  HIV_2015 = format_HIV(OAS_dict, 'HIV_2015')
  HA_bnAb  = {'Total_count': sum([int(HA_Joyce_dict[ID]['Total_count']) for ID in HA_Joyce_dict.keys()])+
                             sum([int(HA_Andrews_dict[ID]['Total_count']) for ID in HA_Andrews_dict.keys()])+
                             sum([int(HA_Andrews_STM_dict[ID]['Total_count']) for ID in HA_Andrews_STM_dict.keys()])+
                             sum([int(HA_McCarthy_dict[ID]['Total_count']) for ID in HA_McCarthy_dict.keys()])+
                             sum([int(HA_Pappas_dict[ID]['Total_count']) for ID in HA_Pappas_dict.keys()]),
              'ILTG_count': sum([int(HA_Joyce_dict[ID]['ILTG_count']) for ID in HA_Joyce_dict.keys()])+
                            sum([int(HA_Andrews_dict[ID]['ILTG_count']) for ID in HA_Andrews_dict.keys()])+
                            sum([int(HA_Andrews_STM_dict[ID]['ILTG_count']) for ID in HA_Andrews_STM_dict.keys()])+
                            sum([int(HA_McCarthy_dict[ID]['ILTG_count']) for ID in HA_McCarthy_dict.keys()])+
                            sum([int(HA_Pappas_dict[ID]['ILTG_count']) for ID in HA_Pappas_dict.keys()]),
              'LRYFDWL_count': sum([int(HA_Joyce_dict[ID]['LRYFDWL_count']) for ID in HA_Joyce_dict.keys()])+
                               sum([int(HA_Andrews_dict[ID]['LRYFDWL_count']) for ID in HA_Andrews_dict.keys()])+
                               sum([int(HA_Andrews_STM_dict[ID]['LRYFDWL_count']) for ID in HA_Andrews_STM_dict.keys()])+
                               sum([int(HA_McCarthy_dict[ID]['LRYFDWL_count']) for ID in HA_McCarthy_dict.keys()])+
                               sum([int(HA_Pappas_dict[ID]['LRYFDWL_count']) for ID in HA_Pappas_dict.keys()])}
  samples = ['Flu HA cross-react Ab', 'MEN Subject 1001', 'MEN Subject 1014',
             'MEN Subject 1018', 'MEN Subject 1020', 'HIV time point 1', 'HIV time point 2', 'HIV time point 3']
  sample_dicts = [HA_bnAb, OAS_dict['MEN_Subj_1001'], OAS_dict['MEN_Subj_1014'],
                  OAS_dict['MEN_Subj_1018'], OAS_dict['MEN_Subj_1020'], HIV_2012, HIV_2014, HIV_2015]
  print "writing: %s" % outfile
  outfile  = open(outfile, 'w')
  outfile.write("\t".join(['Sample','Total_count','ILTG_count','LRYFDWL_count'])+"\n")
  for sample, sample_dict in zip(samples, sample_dicts): 
    outfile.write("\t".join(map(str, [sample, sample_dict['Total_count'], sample_dict['ILTG_count'], sample_dict['LRYFDWL_count']]))+"\n")
  outfile.close()
  

def main():
  outfile  = 'result/Compare_OAS.tsv'
  OAS_dict = TsvWithHeader2Hash('result/Dgene_OAS_summary.tsv')
  HA_Joyce_dict       = TsvWithHeader2Hash('result/Dgene_Joyce_Patient_summary.tsv')
  HA_Andrews_dict     = TsvWithHeader2Hash('result/Dgene_Andrews_SciImmun_Patient_summary.tsv')
  HA_Andrews_STM_dict = TsvWithHeader2Hash('result/Dgene_Andrews_STM_Patient_summary.tsv')
  HA_McCarthy_dict    = TsvWithHeader2Hash('result/Dgene_McCarthy_Patient_summary.tsv')
  HA_Pappas_dict      = TsvWithHeader2Hash('result/Dgene_Pappas_Patient_summary.tsv')
  formatting(OAS_dict, HA_Joyce_dict, HA_Andrews_dict, HA_Andrews_STM_dict, HA_McCarthy_dict, HA_Pappas_dict, outfile)
  

if __name__ == "__main__":
  main()
