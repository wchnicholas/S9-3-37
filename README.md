This README describes the sequence analysis for the S9-3-37 antibody study

## ANALYSIS FOR HA NATURAL VARIANTS
### INPUT FILE
* Fasta/HAdiffSubtypes.aln: HA protein sequences from representative strains of each subtype
* Fasta/Natural\_All\_Subtypes.aln: HA protein sequences retrieved from [GISAID](https://www.gisaid.org/)
* doc/Epitopes.tsv: Epitope information for S9-3-37 and FI6v3
```
python script/extract_motif_from_aln.py
```
  * Input file:
    * Fasta/HAdiffSubtypes.aln
    * doc/Epitopes.tsv
  * Output file: 
    * result/Epitope\_seq\_entropy.tsv
    * Fasta/Motif.aln

## ANALYSIS FOR ANTIBODY SEQUENCES


### INPUT FILE
* 


