import os as os

def HLAMinerClassIIHLAParser(CWD, CurrDir, T, HLAClassIITextFile):
    HLAMinerClassIIHLA = []
    with open((os.path.join(CWD, CurrDir, T, HLAClassIITextFile))) as file:
                    lines = file.readlines()
                    
                    for line in lines:
                        if ("DPA1*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine) #Additional steps to preserve P in the HLA name
                            HLALine1 = HLALine.split('\t')[2].split(',')[0].split(':')[0]
                            HLALine2 = HLALine.split('\t')[2].split(',')[0].split(':')[1].replace("P", "", -1).replace("'", "")
                            HLALine = HLALine1 + ":" + HLALine2
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DPB1*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine) #Additional steps to preserve P in the HLA name
                            HLALine1 = HLALine.split('\t')[2].split(',')[0].split(':')[0]
                            HLALine2 = HLALine.split('\t')[2].split(',')[0].split(':')[1].replace("P", "", -1).replace("'", "")
                            HLALine = HLALine1 + ":" + HLALine2
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DQA1*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DQB1*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRA*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB1*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB2*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB3*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB4*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB5*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB6*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB7*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB8*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
                        elif ("DRB9*" in line) and (not ("Prediction" in line)): 
                            linestart = lines.index(line)
                            HLALine = lines[linestart].replace("'", "")
                            print("HLAMiner$$$$$****************", HLALine)
                            HLALine = HLALine.split('\t')[2].split(',')[0].replace("P", "").replace("'", "")
                            print("Final HLAMiner HLA:", HLALine)
                            HLAMinerClassIIHLA.append(HLALine)
    print("All HLAMiner$$$$$ ****************", HLAMinerClassIIHLA)
    return HLAMinerClassIIHLA #Find how to sort this list
