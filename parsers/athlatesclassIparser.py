import os as os

def AthlatesClassIHLAParser(CWD, CurrDir, T, HLAClassITextFile):
    with open((os.path.join(CWD, CurrDir, T, HLAClassITextFile))) as file:
                    lines = file.readlines()
                    for line in lines:
                        if "Inferred Allelic Pairs" in line:
                            linestart = lines.index(line)
                            try:
                                HLALine = lines[linestart+2]
                                print("****************", HLALine)
                                HLALine = HLALine.split('\t\t')
                                return("HLA-"+ HLALine[0].split(':')[0]+ ":"+ HLALine[0].split(':')[1], "HLA-"+ HLALine[1].split(':')[0]+ ":"+ HLALine[1].split(':')[1]) #use return to snd value back to caller
                            except IndexError:
                                print("The file "+HLAClassITextFile +" may be empty")
