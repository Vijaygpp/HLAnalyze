import os as os

def PolysolverClassIHLAParser(CWD, CurrDir, T, HLAClassITextFile):
    with open((os.path.join(CWD, CurrDir, T, HLAClassITextFile))) as file:
                    lines = file.readlines()
                    for line in lines:
                        if ("HLA-A" in line):
                            linestart = lines.index(line)
                            HLALine = lines[linestart]
                            HLALine = HLALine.upper()
                            print("Polysolver****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            HLALine1 = HLALine[1]
                            HLALine2 = HLALine[2]
                            HLALine1 = HLALine1.split('_')
                            HLALine2 = HLALine2.split('_')
                            print(HLALine1)
                            print(HLALine2)
                            A1 = (HLALine1[0] + "-" + HLALine1[1] + "*" + HLALine1[2] + ":" + HLALine1[3])
                            A2 = (HLALine2[0] + "-" + HLALine2[1] + "*" + HLALine2[2] + ":" + HLALine2[3])
                            print("Polysolver HLA:", A1, A2)
                        
                        elif ("HLA-B" in line):
                            linestart = lines.index(line)
                            HLALine = lines[linestart]
                            HLALine = HLALine.upper()
                            print("Polysolver****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            HLALine1 = HLALine[1]
                            HLALine2 = HLALine[2]
                            HLALine1 = HLALine1.split('_')
                            HLALine2 = HLALine2.split('_')
                            print(HLALine1)
                            print(HLALine2)
                            B1 = (HLALine1[0] + "-" + HLALine1[1] + "*" + HLALine1[2] + ":" + HLALine1[3])
                            B2 = (HLALine2[0] + "-" + HLALine2[1] + "*" + HLALine2[2] + ":" + HLALine2[3])
                            print("Polysolver HLA:", B1, B2)
                        
                        elif ("HLA-C" in line):
                            linestart = lines.index(line)
                            HLALine = lines[linestart]
                            HLALine = HLALine.upper()
                            print("Polysolver****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            HLALine1 = HLALine[1]
                            HLALine2 = HLALine[2]
                            HLALine1 = HLALine1.split('_')
                            HLALine2 = HLALine2.split('_')
                            print(HLALine1)
                            print(HLALine2)
                            C1 = (HLALine1[0] + "-" + HLALine1[1] + "*" + HLALine1[2] + ":" + HLALine1[3])
                            C2 = (HLALine2[0] + "-" + HLALine2[1] + "*" + HLALine2[2] + ":" + HLALine2[3])
                            print("Polysolver HLA:", C1, C2)
                                                
    HLAList = [A1, A2, B1, B2, C1, C2] #use return to snd value back to caller
    return HLAList #Find how to sort this list
