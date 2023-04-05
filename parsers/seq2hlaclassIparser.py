import os as os

def Seq2HLAClassIHLAParser(CWD, CurrDir, T, HLAClassITextFile):
    with open((os.path.join(CWD, CurrDir, T, HLAClassITextFile))) as file:
                    lines = file.readlines()
                    for line in lines:
                        if ("A*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            A1 = ("HLA-" + HLALine[1])
                            A2 = ("HLA-" + HLALine[3])
                        elif ("B*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            B1 = ("HLA-" + HLALine[1])
                            B2 = ("HLA-" + HLALine[3])
                        elif ("C*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            C1 = ("HLA-" + HLALine[1])
                            C2 = ("HLA-" + HLALine[3])
    HLAList = [A1, A2, B1, B2, C1, C2] #use return to snd value back to caller
    print("All Seq2HLA ****************", HLAList)
    return HLAList #Find how to sort this list
