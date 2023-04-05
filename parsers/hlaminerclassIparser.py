import os as os

def HLAMinerClassIHLAParser(CWD, CurrDir, T, HLAClassITextFile):
    HLAMinerClassIHLA = []
    with open((os.path.join(CWD, CurrDir, T, HLAClassITextFile))) as file:
                    lines = file.readlines()
                    
                    for line in lines:
                        if ("\tA*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = "HLA-" + HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIHLA.append(HLALine)
                        elif ("\tB*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = "HLA-" + HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIHLA.append(HLALine)
                        elif ("\tC*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = "HLA-" + HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIHLA.append(HLALine)
    print("All HLAMiner$$$$$ ****************", HLAMinerClassIHLA)
    return HLAMinerClassIHLA #Find how to sort this list
