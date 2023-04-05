import os as os
import pandas as pd

from parsers import polysolverclassIparser

def getHLA(CWD, CurrDir, AllHLATools, PolysolverNormalTumorRNA):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if os.path.isdir(os.path.join(CWD, CurrDir, T)) and ("Polysolver" in T) and ("RNA" in T):
            print("*************************RNA Polysolver Directory is: ", T)
            IntermediateDirectory = os.listdir(os.path.join(CWD, CurrDir, T))
            for Fi in IntermediateDirectory:
                if ("winners" in Fi):
                    PolysolverResultFile = os.path.join(CWD, CurrDir, T, Fi)
                    print("Polysolver RNA result file is: ", PolysolverResultFile)
                    PolysolverRNAHLA = polysolverclassIparser.PolysolverClassIHLAParser(CWD, CurrDir, T, PolysolverResultFile)
                    print(PolysolverRNAHLA)
                    PolysolverNormalTumorRNA['RNA-Tumor'] = PolysolverRNAHLA
    return [PolysolverNormalTumorRNA]