# HLAnalyze
A utility for analysis of consensus HLA typing results using multiple HLA typing software and tissue sources.

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

Important: The file names and directory structure should follow as given in  HLAnalyze-DemoSample/Sample01-ConsensusHLA/ directory. Built and tested on linux.


