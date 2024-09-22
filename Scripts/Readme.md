# Scripts
The directory contains script files and a brief description of what each script is developed for.
The Readme.md file outlines major steps of the analysis and how scripts are supposed to be used.

### I. Pre-processing

* Put Multiple Sequence Alignments (MSAs) in a fasta format into a separate folder.
> [!NOTE]
Re-name the sequences in the alignment files if necessary using `hhsuite_alnsfasta_rename.py`. The renamed fasta alignment file will have .faa extension.
In HH-suite3, the fasta header line of the first sequence in each MSA file becomes the name for all the entities generated from this MSA file by default.
If a given alignment file is used for creating a Hidden Markov Model (HMM), it is useful to include the HMM name into the fasta header line for each sequence in the MSA file. Please see an example below.

The initial fasta header line:
> \>NPY1R_HUMAN/57-320

The renamed fasta header line:
> \>PF00001.26 ### NPY1R_HUMAN/57-320

The fasta alignments can be converted to .a3m alignment files. The .a3m format is considered to be more space effecient. In practice, the alignment files in .a3m files occupy about 2/3 of space that is needed for storing the same alignments in .fasta format. For example, 22,363 alignment files utilized for creating refDB (please see the description below) in .fasta format occupy ~450Mb, and in .a3m they occupy ~300 Mb. To convert all .fasta alignment in the current directory, the following command is used:  

`reformat.pl fas a3m '*.faa’ .a3m`

or

`reformat.pl fas a3m '*.faa’ .a3m > a3m_info.txt`

The second version of this command allows us to store the statistics (e.g., the number of sequences in each alignment file) generated during the conversion of the files in a separate txt file rather than to output on screen.

Also, it is useful to move all the newly generated .a3m files into a separate directory:
```
mkdir A3M
mv ./*.a3m ./A3M
```

To create HMM named HMM1 from MSA in .a3m format (the name of the HMM in .hhm file is the name of the first sequence in the MSA file):
```
hhmake -i HMM1.a3m -o HMM1.hhm
```

To analyze similarity between HMMs and\or MSAs, HH-suite3 provides three main opportunities: hhalign, hhsearch, and hhblits.
The first option (hhalign) is intended to compare two entities, and it does not require using a database.
The other two options (hhsearch and hhblits) do require creation of a custom database and/or use of the precompiled databases available for download with HH-suite.
I will demonstrate the creation of a custom database using refGB as an example.
The refDB is created based on a set of MSAs from our custom Phage Annotation Toolkit (PAT) HMM collection and seed alignments of the most recent release of Pfam HMM collection (Release 37). There are 22,363 MSAs in total. Each HH-suite database contains six files:
(1)
(2)
(3)
(4)
(5)
(6)

Below is step-by-step description of the process of creating these six files for refGB from a set of MSA files in .a3m format.





### II. Similarity analysis


### III. Exploring the results
