# HLAnalyze
A utility for analysis of consensus HLA typing results using multiple HLA typing software and tissue sources.

Extracts and compiles HLA-typing calls from five HLA-typing software [ATHLATES, OptiType, Polysolver, Seq2HLA and HLAminer] and three high throughput data sources [Tumor-DNA, Normal-DNA, Tumor-RNA] in analysis ready form and creates a ppt file for analysis and finalization of consensus HLA-type calls. 

Run following for use instructions:

python3 createHLAPPT.py --help

usage: createHLAPPT.py [-h] [-i INPUTDIR] [-s SAMPLEID]

help message

optional arguments:
  -h, --help            show this help message and exit
  -i INPUTDIR, --InputDir INPUTDIR
                        Input directory
  -s SAMPLEID, --SampleID SAMPLEID
                        Sample ID
                        

Example usage:

python3 createHLAPPT.py -i inputdirectory/ -s samplename

Use Demo Sample data:

cd HLAnalyze-DemoSample 

python3 createHLAPPT.py -i Sample01-ConsensusHLA/ -s Sample01

Important: The file names and directory structure should follow as given in the HLAnalyze-DemoSample/Sample01-ConsensusHLA/ directory. This software was built and tested on linux.

Sample01-ConsensusHLA/

├── HLA-ATHLATES-Sample01-Repeat-N

│   ├── Sample01-Repeat-N-Athlates-HLA-A.typing.txt

│   ├── Sample01-Repeat-N-Athlates-HLA-B.typing.txt

│   ├── Sample01-Repeat-N-Athlates-HLA-C.typing.txt

│   ├── Sample01-Repeat-N-Athlates-HLA-DPA1.typing.txt

│   ├── Sample01-Repeat-N-Athlates-HLA-DPB1.typing.txt

│   ├── Sample01-Repeat-N-Athlates-HLA-DQA1.typing.txt

│   ├── Sample01-Repeat-N-Athlates-HLA-DQB1.typing.txt

│   ├── Sample01-Repeat-N-Athlates-HLA-DRA.typing.txt

│   └── Sample01-Repeat-N-Athlates-HLA-DRB1.typing.txt

├── HLA-ATHLATES-Sample01-Repeat-R

├── HLA-ATHLATES-Sample01-Repeat-T

│   ├── Sample01-Repeat-T-Athlates-HLA-A.typing.txt

│   ├── Sample01-Repeat-T-Athlates-HLA-B.typing.txt

│   ├── Sample01-Repeat-T-Athlates-HLA-C.typing.txt

│   ├── Sample01-Repeat-T-Athlates-HLA-DPA1.typing.txt

│   ├── Sample01-Repeat-T-Athlates-HLA-DPB1.typing.txt

│   ├── Sample01-Repeat-T-Athlates-HLA-DQA1.typing.txt

│   ├── Sample01-Repeat-T-Athlates-HLA-DQB1.typing.txt

│   ├── Sample01-Repeat-T-Athlates-HLA-DRA.typing.txt

│   └── Sample01-Repeat-T-Athlates-HLA-DRB1.typing.txt

├── HLA-OptiType-Normal-Sample01

│   └── 2022_12_21_19_58_45

│       └── 2022_12_21_19_58_45_result.tsv

├── HLA-OptiType-RNA-Sample01

│   └── 2022_12_21_20_34_57

│       └── 2022_12_21_20_34_57_result.tsv

├── HLA-OptiType-Tumor-Sample01

│   └── 2022_12_21_07_04_23

│       └── 2022_12_21_07_04_23_result.tsv

├── HLA-Polysolver-Normal-Sample01

│   └── winners.hla.txt

├── HLA-Polysolver-RNA-Sample01

│   └── winners.hla.txt

├── HLA-Polysolver-Tumor-Sample01

│   └── winners.hla.txt

├── HLA-Seq2HLA-Normal-Sample01

│   ├── HLA-Seq2HLA-Normal-Sample01-ClassI-class.HLAgenotype4digits

│   └── HLA-Seq2HLA-Normal-Sample01-ClassII.HLAgenotype4digits

├── HLA-Seq2HLA-RNA-Sample01

│   ├── HLA-Seq2HLA-RNA-Sample01-ClassI-class.HLAgenotype4digits

│   └── HLA-Seq2HLA-RNA-Sample01-ClassII.HLAgenotype4digits

└── HLA-Seq2HLA-Tumor-Sample01

├── HLA-Seq2HLA-Tumor-Sample01-ClassI-class.HLAgenotype4digits

└── HLA-Seq2HLA-Tumor-Sample01-ClassII.HLAgenotype4digits

