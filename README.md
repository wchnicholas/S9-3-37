This README describes the sequence analysis for the S9-3-37 antibody study

## ANALYSIS FOR HA NATURAL VARIANTS
### INPUT FILE
* Fasta/HAdiffSubtypes.aln: HA protein sequences from representative strains of each subtype
* Fasta/Natural\_All\_Subtypes.aln: HA protein sequences retrieved from [GISAID](https://www.gisaid.org/)
* doc/Epitopes.tsv: Epitope information for S9-3-37 and FI6v3

### DATA PROCESSING
1. Extract amino acid identity for each strain at S9-3-37/FI6v3 epitope residues
```
python script/extract_motif_from_aln.py
```
  * Input file:
    * Fasta/HAdiffSubtypes.aln
    * doc/Epitopes.tsv
  * Output file: 
    * result/Epitope\_seq\_entropy.tsv
    * Fasta/Motif.aln

2. Extract amino acid identity for each strain at residues of interset
```
python script/extract_resi_from_aln.py
```
  * Input file: Fasta/Natural\_All\_Subtypes.aln
  * Output file:
    * result/Resi38.tsv
    * result/Resi50.tsv

### PLOTTING
1. Plot sequence entropy of S9-3-37/FI6v3 epitope residues
```
Rscript plot_entropy.R
```
  * Input file: result/Epitope\_seq\_entropy.tsv
  * Output file: graph/entropy\_distribution.png

2. Plot sequence logos for residues of interset
```
script/seqlogo_resi.sh
```
  * Input file: 
    * result/Resi38.tsv
    * result/Resi50.tsv
  * Output file:
    * graph/Resi38\_H\*.png
    * graph/Resi50\_H\*.png

## ANALYSIS FOR ANTIBODY SEQUENCES
### INPUT FILE
* 


