This README describes the sequence analysis for the S9-3-37 antibody study. The sequence analysis is divided into two parts. Part I describes the analysis for influenza hemagglutinin (HA) natural variants. Part II describes the analysis for antibody sequences. 
## PART I: ANALYSIS FOR HA NATURAL VARIANTS
### INPUT FILE
* Fasta/HAdiffSubtypes.aln: HA protein sequences from representative strains of each subtype
* Fasta/Natural\_All\_Subtypes.aln: HA protein sequences retrieved from [GISAID](https://www.gisaid.org/)
* doc/Epitopes.tsv: Epitope information for S9-3-37 and FI6v3

### DATA PROCESSING
1. To extract amino acid identity for each strain at S9-3-37/FI6v3 epitope residues
```
python script/extract_motif_from_aln.py
```
  * Input file:
    * Fasta/HAdiffSubtypes.aln
    * doc/Epitopes.tsv
  * Output file: 
    * result/Epitope\_seq\_entropy.tsv
    * Fasta/Motif.aln

2. To extract amino acid identity for each strain at residues of interset
```
python script/extract_resi_from_aln.py
```
  * Input file: Fasta/Natural\_All\_Subtypes.aln
  * Output file:
    * result/Resi38.tsv
    * result/Resi50.tsv

### PLOTTING
1. To plot sequence entropy of S9-3-37/FI6v3 epitope residues
```
Rscript script/plot_entropy.R
```
  * Input file: result/Epitope\_seq\_entropy.tsv
  * Output file: graph/entropy\_distribution.png

2. To plot sequence logos for residues of interset
```
bash script/seqlogo_resi.sh
```
  * Input file: 
    * result/Resi38.tsv
    * result/Resi50.tsv
  * Output file:
    * graph/Resi38\_H\*.png
    * graph/Resi50\_H\*.png

## PART II: ANALYSIS FOR ANTIBODY SEQUENCES
### INPUT FILE
* data/Andrews\_STM\_StemAbList.tsv: From Table S3 and Table S4 in [Andrews et al. 2015](http://stm.sciencemag.org/content/7/316/316ra192.full) 
* data/Andrews\_SciImmun.tsv: From Table S7 in [Andrews et al. 2017](http://immunology.sciencemag.org/content/suppl/2017/07/10/2.13.eaan2676.DC1)
* data/Donor1.tsv: From 
* data/Donor2.tsv: From
* data/Donor3.tsv: From
* data/Pappas\_StemAbList.tsv: From Figure S1 of [Pappas et al. 2014](https://www.nature.com/articles/nature13764#methods)
* data/Subj1.tsv: From
* data/Subj16.tsv: From
* data/Subj31.tsv: From
* data/Subj36.tsv: From
* data/Subj54.tsv: From
* data/Subj56.tsv: From 
* result/Dgene\_McCarthy\_Patient\_summary.tsv: From Figure S4 in [McCarthy et al. 2018](https://www.cell.com/immunity/fulltext/S1074-7613(17)30538-1)
* data/HIV\_bNAber.fasta: Nucleotide sequences for HIV bnAbs. Downloaded from [bNAber database](https://academic.oup.com/nar/article/42/D1/D1133/1048421)
* data/HIV\_bNAber.tsv: Information for germline usage of HIV bnAbs. Output from [IgBlast](https://www.ncbi.nlm.nih.gov/igblast/index.cgi)
* data/OAS\_info.tsv: Sample information for the next-generation sequencing data downloaded from [Observed Antibody Space](http://antibodymap.org./oas)

### DATA PROCESSING
1. To summarize ##

### PLOTTING
