import os as os

def Seq2HLAClassIIHLAParser(CWD, CurrDir, T, HLAClassIITextFile):
    D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12 = ["nan"] * 12
    with open((os.path.join(CWD, CurrDir, T, HLAClassIITextFile))) as file:
                    lines = file.readlines()
                    for line in lines:
                        if ("DQA1*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            D1 = (HLALine[1])
                            D2 = (HLALine[3])
                        elif ("DQB1*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            D3 = (HLALine[1])
                            D4 = (HLALine[3])
                        elif ("DRB1*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            D5 = (HLALine[1])
                            D6 = (HLALine[3])
                        elif ("DRA*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            D7 = (HLALine[1])
                            D8 = (HLALine[3])
                        elif ("DPA1*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            D9 = (HLALine[1])
                            D10 = (HLALine[3])
                        elif ("DPB1*" in line): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("Seq2HLA****************", HLALine)
                            HLALine = HLALine.split('\t')
                            print(HLALine)
                            D11 = (HLALine[1])
                            D12 = (HLALine[3])
    HLAList = [D1, D2, D3, D4, D5, D6, D7, D8, D9, D10, D11, D12] #use return to snd value back to caller
    print("All Seq2HLA ****************", HLAList)
    return HLAList #Find how to sort this list
