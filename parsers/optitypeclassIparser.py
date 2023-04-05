import os as os

def OptiTypeClassIHLAParser(CWD, CurrDir, T, HLAClassITextFile):
    with open((os.path.join(CWD, CurrDir, T, HLAClassITextFile))) as file:
                    lines = file.readlines()
                    for line in lines:
                        if ("A*" in line) and ("B*" in line) and ("C*" in line):
                            linestart = lines.index(line)
                            HLALine = lines[linestart]
                            print("****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            A1 = ("HLA-" + HLALine[1])
                            A2 = ("HLA-" + HLALine[2])
                            B1 = ("HLA-" + HLALine[3])
                            B2 = ("HLA-" + HLALine[4])
                            C1 = ("HLA-" + HLALine[5])
                            C2 = ("HLA-" + HLALine[6])
    HLAList = [A1, A2, B1, B2, C1, C2] #use return to snd value back to caller
    return HLAList #Find how to sort this list
