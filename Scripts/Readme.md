# Scripts
The directory contains script files and a brief description of what each script is developed for.
The Readme.md file outlines major steps of the analysis and how scripts are supposed to be used.

### I. Pre-processing

* Put Multiple Sequence Alignments (MSAs) in a fasta format into a separate folder. Note: re-name the sequences in the alignment files if necessary.
  By default, the fasta header line of the first sequence in each MSA file becomes the name for all the entities generated from this MSA file by tools in HH-suite3.
  If a given alignment file is used for creating a Hidden Markov Model (HMM), it is useful to include the HMM name into the fasta header line for each sequence in the MSA file. Please see an example below.

The initial fasta header line:
>NPY1R_HUMAN/57-320
The renamed fasta header line:
>PF00001.26 ### NPY1R_HUMAN/57-320

### II. Similarity analysis


### III. Exploring the results
