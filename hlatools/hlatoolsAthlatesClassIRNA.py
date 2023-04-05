import os as os
import pandas as pd

from parsers import athlatesclassIparser

def getHLA(CWD, CurrDir, AllHLATools, AthlatesClassI):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if os.path.isdir(os.path.join(CWD, CurrDir, T)) and ("ATHLATES" in T):
            print("HLADIR contains: ", os.listdir(os.path.join(CWD, CurrDir, T)))
            HLADIR = os.listdir(os.path.join(CWD, CurrDir, T))
            for D in HLADIR:
                print(D)
                if (("Athlates" in D) and ("-R-" in D) and ("HLA-A" in D)):
                    print("this is Athlates A typing rna file") #Code was here
                    AthlatesClassIRNAHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIRNAHLA)
                    try:
                        AthlatesClassI["RNA-Tumor"][0] = AthlatesClassIRNAHLA[0]
                        AthlatesClassI["RNA-Tumor"][1] = AthlatesClassIRNAHLA[1]
                    except TypeError:
                        print("HLA-A typing for RNA not available")
                        AthlatesClassI["RNA-Tumor"][0] = "HLA-A NA"
                        AthlatesClassI["RNA-Tumor"][1] = "HLA-A NA"
                        
                elif (("Athlates" in D) and ("-R-" in D) and ("HLA-B" in D)):
                    print("this is Athlates B typing rna file")
                    AthlatesClassIRNAHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIRNAHLA)
                    try:
                        AthlatesClassI["RNA-Tumor"][2] = AthlatesClassIRNAHLA[0]
                        AthlatesClassI["RNA-Tumor"][3] = AthlatesClassIRNAHLA[1]
                    except TypeError:
                        print("HLA-B typing for RNA not available")
                        AthlatesClassI["RNA-Tumor"][2] = "HLA-B NA"
                        AthlatesClassI["RNA-Tumor"][3] = "HLA-B NA"
                    
                elif (("Athlates" in D) and ("-R-" in D) and ("HLA-C" in D)):
                    print("this is Athlates C typing rna file")
                    AthlatesClassIRNAHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIRNAHLA)
                    try:
                        AthlatesClassI["RNA-Tumor"][4] = AthlatesClassIRNAHLA[0]
                        AthlatesClassI["RNA-Tumor"][5] = AthlatesClassIRNAHLA[1]
                    except TypeError:
                        print("HLA-C typing for RNA not available")
                        AthlatesClassI["RNA-Tumor"][4] = "HLA-C NA"
                        AthlatesClassI["RNA-Tumor"][5] = "HLA-C NA"
    return [AthlatesClassI]
