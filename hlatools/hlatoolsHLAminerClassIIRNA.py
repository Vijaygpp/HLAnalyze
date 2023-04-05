import os as os
import pandas as pd

from parsers import hlaminerclassIparser

def getHLA(CWD, CurrDir, AllHLATools, HLAMinerClassIIRNATumorHLA):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if (("HLAminer_HPRA" in T) and ("csv" in T)):
            HLAMinerResultFile = os.path.join(CWD, CurrDir, T)
            print("HLAMiner RNA HLA result file is: ", HLAMinerResultFile)
            HLAMinerClassIIRNATumorHLA = HLAMinerClassIIRNATumorHLA + hlaminerclassIIparser.HLAMinerClassIIHLAParser(CWD, CurrDir, T, HLAMinerResultFile)
            print("HLAminer Class II @@@@@@@@@@@@@@@", HLAMinerClassIIRNATumorHLA)
    return [HLAMinerClassIIRNATumorHLA]
