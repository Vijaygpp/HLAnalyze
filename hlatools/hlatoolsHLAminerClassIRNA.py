import os as os
import pandas as pd

from parsers import hlaminerclassIparser

def getHLA(CWD, CurrDir, AllHLATools, HLAMinerClassIRNATumorHLA):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if (("HLAminer_HPRA" in T) and ("csv" in T)):
            HLAMinerResultFile = os.path.join(CWD, CurrDir, T)
            print("HLAMiner RNA HLA result file is: ", HLAMinerResultFile)
            HLAMinerClassIRNATumorHLA = HLAMinerClassIRNATumorHLA + hlaminerclassIparser.HLAMinerClassIHLAParser(CWD, CurrDir, T, HLAMinerResultFile)
            print("HLAminer Class I @@@@@@@@@@@@@@@", HLAMinerClassIRNATumorHLA)
    return [HLAMinerClassIRNATumorHLA]
