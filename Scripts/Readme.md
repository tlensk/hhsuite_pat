# Scripts
The directory contains script files and a brief description of what each script is developed for.
The Readme.md file outlines major steps of the analysis and how scripts are supposed to be used.
It is assumed that HH-suite3<sup>1</sup> is already installed. For installation instructions, please visit https://github.com/soedinglab/hh-suite and refer to the HH-suite3 User's Guide: https://github.com/soedinglab/hh-suite/wiki.

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
To compare two HMMs in .hhm format:
```
hhalign -i PT001001.hhm -t PT002001.hhm -o cmp1.hhr
```


To analyze similarity between HMMs and\or MSAs, HH-suite3 provides three main opportunities: hhalign, hhsearch, and hhblits.
The first option (hhalign) is intended to compare two entities, and it does not require using a database.
The other two options (hhsearch and hhblits) do require creation of a custom database and/or use of the precompiled databases available for download with HH-suite.
I will demonstrate the creation of a custom database using refGB as an example.
The refDB is created based on a set of MSAs from our custom Phage Annotation Toolkit (PAT) HMM collection and seed alignments of the most recent release of Pfam HMM collection (Release 37). There are 22,363 MSAs in total. Each HH-suite database contains six files:

(1) refDB_a3m.ffdata - a joint packed file with the alignments in .a3m format;

(2) refDB_a3m.ffindex - an index file for the joint packed alignment file;

(3) refDB_hhm.ffdata - a joint packed file with HMMs in .hhm format (HH-suite3 format for HMMs);

(4) refDB_hhm.ffindex - an index file for the joint packed HMM file;

(5) refDB_cs219.ffdata - a joint packed file with column-state sequences for prefiltering;

(6) refDB_cs219.ffindex - an index file for the joint packed column-state sequence file.

Below is step-by-step description of the process of creating these six files for refGB from a set of MSA files in .a3m format.
All the following commands are executed in the current directory that contains the A3M sub-directory with all the alignment files unless stated otherwise.

__Step 1.__ To create a joint .a3m file and its index file:
```
ffindex_build -as refDB_a3m.ffdata refDB_a3m.ffindex A3M
```

__Step 2.__ To create a joint .hhm file and its index:
```
ffindex_apply refDB_a3m.ff{data,index} -i refDB_hhm.ffindex -d refDB_hhm.ffdata -- hhmake -i stdin -o stdout -v 0
```
__Step 3.__ To create a joint column-state sequence file and its index:
```
/home/hhsuite/hhsuite/bin/cstranslate -i refDB_a3m -A ./cs219.lib -o refDB_cs219 -b -f -I a3m
```
> [!NOTE]
This step requires cs219.lib. If this library is not present in the existing installation of HH-suite3, it can be downloaded directly using the following link: https://github.com/soedinglab/hh-suite/blob/master/data/cs219.lib and saved to the current directory.

After all the required six files are generated, it is possible to query the newly created database using MSA and HMM.

To query refDB using __hhsearch__ with MSA in .fasta format:
```
hhsearch -i PT001001.faa -d refDB  -o faa_results_file_s
```

To query refDB using __hhblits__ with MSA in .fasta format:
```
hhblits -i ./faa/PT001001.faa -d refDB -n 1 -o faa_results_file
```

To query refDB using __hhsearch__ with HHM in .hhm format:
```
hhsearch -i PT001001.hhm -d refDB  -o hhm_results_file_s
```

To query refDB using __hhblits__ with HMM in .hhm format:
```
hhblits -i PT001001.hhm -d refDB -n 1 -o hhm_results_file
```

### II. Similarity analysis


### III. Exploring the results


### References

[1] Steinegger, M., Meier, M., Mirdita, M., Vöhringer, H., Haunsberger, S. J., & Söding, J. (2019). HH-suite3 for fast remote homology detection and deep protein annotation. BMC bioinformatics, 20, 1-15.
