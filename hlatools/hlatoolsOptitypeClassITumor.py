import os as os
import pandas as pd

from parsers import optitypeclassIparser

def getHLA(CWD, CurrDir, AllHLATools, OptiTypeNormalTumorRNA):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if os.path.isdir(os.path.join(CWD, CurrDir, T)) and ("OptiType" in T) and ("Tumor" in T):
            print("*************************Tumor OptiType Directory is: ", T)
            IntermediateDirectory = os.listdir(os.path.join(CWD, CurrDir, T))
            FinalDirectory = os.listdir(os.path.join(CWD, CurrDir, T, IntermediateDirectory[0]))
            print("FinalDirectory", FinalDirectory)
            for Fi in FinalDirectory:
                if ("result" in Fi):
                    OptitypeResultFile = os.path.join(CWD, CurrDir, T, IntermediateDirectory[0], Fi)
                    print("OptiType Tumor result file is: ", OptitypeResultFile)
                    OptiTypeTumorHLA = optitypeclassIparser.OptiTypeClassIHLAParser(CWD, CurrDir, T, OptitypeResultFile)
                    print(OptiTypeTumorHLA)
                    OptiTypeNormalTumorRNA['DNA-Tumor'] = OptiTypeTumorHLA
    return [OptiTypeNormalTumorRNA]
        
