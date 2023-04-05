import os as os
import pandas as pd

from parsers import polysolverclassIparser

def getHLA(CWD, CurrDir, AllHLATools, PolysolverNormalTumorRNA):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if os.path.isdir(os.path.join(CWD, CurrDir, T)) and ("Polysolver" in T) and ("Normal" in T):
            print("*************************Normal Polysolver Directory is: ", T)
            IntermediateDirectory = os.listdir(os.path.join(CWD, CurrDir, T))
            for Fi in IntermediateDirectory:
                if ("winners" in Fi):
                    PolysolverResultFile = os.path.join(CWD, CurrDir, T, Fi)
                    print("Polysolver Normal result file is: ", PolysolverResultFile)
                    PolysolverNormalHLA = polysolverclassIparser.PolysolverClassIHLAParser(CWD, CurrDir, T, PolysolverResultFile)
                    print(PolysolverNormalHLA)
                    PolysolverNormalTumorRNA['DNA-Normal'] = PolysolverNormalHLA
    return [PolysolverNormalTumorRNA]



