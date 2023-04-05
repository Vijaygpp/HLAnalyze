import os as os
import pandas as pd

from parsers import seq2hlaclassIparser

def getHLA(CWD, CurrDir, AllHLATools, Seq2HLAClassINormalTumorRNA):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if os.path.isdir(os.path.join(CWD, CurrDir, T)) and ("Seq2HLA" in T) and ("RNA" in T):
            print("*************************RNA Seq2HLA Directory is: ", T)
            IntermediateDirectory = os.listdir(os.path.join(CWD, CurrDir, T))
            for Fi in IntermediateDirectory:
                if (("Seq2HLA" in Fi) and ("RNA" in Fi) and ("ClassI-class.HLAgenotype4digits" in Fi)):
                    Seq2HLAResultFile = os.path.join(CWD, CurrDir, T, Fi)
                    print("Seq2HLA RNA result file is: ", Seq2HLAResultFile)
                    Seq2HLARNAHLA = seq2hlaclassIparser.Seq2HLAClassIHLAParser(CWD, CurrDir, T, Seq2HLAResultFile)
                    print("&&&&&&&&&&&&&&&&&&", Seq2HLARNAHLA)
                    Seq2HLAClassINormalTumorRNA['RNA-Tumor'] = Seq2HLARNAHLA
    return [Seq2HLAClassINormalTumorRNA]