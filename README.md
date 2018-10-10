This README describes the scripts used for the sequence analysis in:   
[Recurring and Adaptable Binding Motifs in Broadly Neutralizing Antibodies to Influenza Virus Are Encoded on the D3-9 Segment of the Ig Gene](https://www.cell.com/cell-host-microbe/fulltext/S1931-3128(18)30494-3)

The sequence analysis is divided into two parts. [Part I](https://github.com/wchnicholas/S9-3-37#part-i-analysis-for-ha-natural-variants) describes the analysis for influenza hemagglutinin (HA) natural variants. [Part II](https://github.com/wchnicholas/S9-3-37#part-ii-analysis-for-antibody-sequences) describes the analysis for antibody sequences. 
## PART I: ANALYSIS OF HA NATURAL VARIANTS
### INPUT FILES
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

## PART II: ANALYSIS OF ANTIBODY SEQUENCES
### INPUT FILES
* data/Subj1.tsv: From Table S3 in [Joyce et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27453470)
* data/Subj16.tsv: From Table S3 in [Joyce et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27453470)
* data/Subj31.tsv: From Table S3 in [Joyce et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27453470)
* data/Subj36.tsv: From Table S3 in [Joyce et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27453470)
* data/Subj54.tsv: From Table S3 in [Joyce et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27453470)
* data/Subj56.tsv: From Table S3 in [Joyce et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27453470)
* data/Andrews\_STM\_StemAbList.tsv: From Table S3 and Table S4 in [Andrews et al. 2015](https://www.ncbi.nlm.nih.gov/pubmed/26631631) 
* data/Andrews\_SciImmun.tsv: From Table S7 in [Andrews et al. 2017](https://www.ncbi.nlm.nih.gov/pubmed/28783708)
* data/Pappas\_StemAbList.tsv: From Figure S1 of [Pappas et al. 2014](https://www.ncbi.nlm.nih.gov/pubmed/25296253)
* result/Dgene\_McCarthy\_Patient\_summary.tsv: From Figure S4 in [McCarthy et al. 2018](https://www.ncbi.nlm.nih.gov/pubmed/29343437)
* data/Donor1.tsv: From Supplementary Data Set 1 in [DeKosky et al. 2015](https://www.ncbi.nlm.nih.gov/pubmed/25501908)
* data/Donor2.tsv: From Supplementary Data Set 1 in [DeKosky et al. 2015](https://www.ncbi.nlm.nih.gov/pubmed/25501908)
* data/Donor3.tsv: From Supplementary Data Set 1 in [DeKosky et al. 2015](https://www.ncbi.nlm.nih.gov/pubmed/25501908)
* data/HIV\_bNAber.fasta: Nucleotide sequences for HIV bnAbs. Downloaded from [bNAber database](https://www.ncbi.nlm.nih.gov/pubmed/24214957)
* data/HIV\_bNAber.tsv: Information for germline usage of HIV bnAbs. Output from [IgBlast](https://www.ncbi.nlm.nih.gov/igblast/index.cgi)

### ADDITIONAL DATASETS
To download the next-generation sequencing data from [Observed Antibody Space](http://antibodymap.org./oas). Data from two studies [Huang et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27851912) and [Galson et al. 2015](https://www.ncbi.nlm.nih.gov/pubmed/25976772) were downloaded. Downloaded data should be placed in json/ folder as .gz files. 
```
bash script/bulk_download.sh
mv *.gz json/
```
  * Sample IDs are described in data/OAS\_info.tsv

### DATA PROCESSING
1. To construct summary tables for D3-9 gene classification
```
python script/Parse_Patient_Joyce.py
python script/Parse_Patient_Andrews_STM.py
python script/Parse_Patient_Andrews_SciImmun.py
python script/Parse_Patient_Pappas.py
python script/Parse_Donor_DeKosky.py
python script/Parse_HIVbnAb.py
python script/Parse_OAS.py
```
  * Input file:
    * data/Subj\*.tsv
    * data/Andrews\_STM\_StemAbList.tsv
    * data/data/Andrews\_SciImmun.tsv
    * data/Pappas\_StemAbList.tsv
    * data/Donor\*.tsv
    * data/HIV\_bNAber.tsv
    * data/OAS\_info.tsv
    * json/\*.gz
  * Output file:
    * result/HD39\_\*.tsv
    * result/Dgene\_\*.tsv

2. To format the data for plotting
```
python script/Format_OAS_plot.py
```
  * Input file: result/Dgene\_\*.tsv
  * Output file: result/Compare\_OAS.tsv

### PLOTTING
1. To plot the D3-9 gene usage of the six subjects in [Joyce et al. 2016](https://www.ncbi.nlm.nih.gov/pubmed/27453470)
```
Rscript script/Plot_Dgene_usage_Joyce_Patient.R
```
  * Input file: result/Dgene\_Joyce\_Patient\_summary.tsv
  * Output file:
    * graph/HD39\_usage\_Joyce\_\*.png
    * graph/HD39\_Joyce\_Patient\_usage.png

2. To plot the D3-9 gene usage in other datasets
```
Rscript script/Plot_Dgene_usage_Andrews_SciImmun_Patient.R
Rscript script/Plot_Dgene_usage_Andrews_STM_Patient.R
Rscript script/Plot_Dgene_usage_Pappas.R
Rscript script/Plot_Dgene_usage_DeKosky_Donor.R
Rscript script/Plot_Dgene_usage_HIV.R
```
  * Input file: result/Dgene\_\*.tsv
  * Output file: graph/HD39\_\*.png

3. To plot the frequency of prevalence of 31.b.09-like (ILTG motif) and S9-3-37-like (LXYFXWL motif) CDR H3 in different samples
```
Rscript script/Plot_Dgene_usage_OAS.R
```
  * Input file: result/Compare\_OAS.tsv
  * Output file: graph/Compare\_OAS.png
