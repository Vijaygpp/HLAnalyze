import os as os
import pandas as pd

from parsers import seq2hlaclassIIparser

def getHLA(CWD, CurrDir, AllHLATools, Seq2HLAClassIINormalTumorRNA):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if os.path.isdir(os.path.join(CWD, CurrDir, T)) and ("Seq2HLA" in T) and ("Normal" in T):
            print("*************************Normal Seq2HLA Directory is: ", T)
            IntermediateDirectory = os.listdir(os.path.join(CWD, CurrDir, T))
            for Fi in IntermediateDirectory:
                if (("Seq2HLA" in Fi) and ("Normal" in Fi) and ("ClassII.HLAgenotype4digits" in Fi)):
                    Seq2HLAResultFile = os.path.join(CWD, CurrDir, T, Fi)
                    print("Seq2HLA Normal result file is: ", Seq2HLAResultFile)
                    Seq2HLANormalHLA = seq2hlaclassIIparser.Seq2HLAClassIIHLAParser(CWD, CurrDir, T, Seq2HLAResultFile)
                    print("&&&&&&&&&&&&&&&&&&", Seq2HLANormalHLA)
                    Seq2HLAClassIINormalTumorRNA['DNA-Normal'] = Seq2HLANormalHLA
    return [Seq2HLAClassIINormalTumorRNA]