import os as os
import pandas as pd

from parsers import seq2hlaclassIparser

def getHLA(CWD, CurrDir, AllHLATools, Seq2HLAClassINormalTumorRNA):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if os.path.isdir(os.path.join(CWD, CurrDir, T)) and ("Seq2HLA" in T) and ("Normal" in T):
            print("*************************Normal Seq2HLA Directory is: ", T)
            IntermediateDirectory = os.listdir(os.path.join(CWD, CurrDir, T))
            for Fi in IntermediateDirectory:
                if (("Seq2HLA" in Fi) and ("Normal" in Fi) and ("ClassI-class.HLAgenotype4digits" in Fi)):
                    Seq2HLAResultFile = os.path.join(CWD, CurrDir, T, Fi)
                    print("Seq2HLA Normal result file is: ", Seq2HLAResultFile)
                    Seq2HLANormalHLA = seq2hlaclassIparser.Seq2HLAClassIHLAParser(CWD, CurrDir, T, Seq2HLAResultFile)
                    print("&&&&&&&&&&&&&&&&&&", Seq2HLANormalHLA)
                    Seq2HLAClassINormalTumorRNA['DNA-Normal'] = Seq2HLANormalHLA
    return [Seq2HLAClassINormalTumorRNA]