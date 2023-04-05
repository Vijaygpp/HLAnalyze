import os as os

def AthlatesClassIIHLAParser(CWD, CurrDir, T, HLAClassIITextFile):
    with open((os.path.join(CWD, CurrDir, T, HLAClassIITextFile))) as file:
                    lines = file.readlines()
                    for line in lines:
                        if "Inferred Allelic Pairs" in line:
                            linestart = lines.index(line)
                            try:
                                HLALine = lines[linestart+2]
                                print("****************", HLALine)
                                HLALine = HLALine.split('\t\t')
                                return(HLALine[0].split(':')[0]+ ":"+ HLALine[0].split(':')[1], HLALine[1].split(':')[0]+ ":"+ HLALine[1].split(':')[1]) #use return to send value back to caller
                            except IndexError:
                                print("The file "+HLAClassITextFile +" may be empty")
