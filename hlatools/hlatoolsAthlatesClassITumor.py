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
                if (("Athlates" in D) and ("-T-" in D) and ("HLA-A" in D)):
                    print("this is Athlates A typing tumor file") #Code was here
                    AthlatesClassITumorHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassITumorHLA)
                    try:
                        AthlatesClassI["DNA-Tumor"][0] = AthlatesClassITumorHLA[0]
                        AthlatesClassI["DNA-Tumor"][1] = AthlatesClassITumorHLA[1]
                    except TypeError:
                        print("HLA-A typing for tumor not available")
                        AthlatesClassI["DNA-Tumor"][0] = "HLA-A NA"
                        AthlatesClassI["DNA-Tumor"][1] = "HLA-A NA"

                        
                elif (("Athlates" in D) and ("-T-" in D) and ("HLA-B" in D)):
                    print("this is Athlates B typing tumor file")
                    AthlatesClassITumorHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassITumorHLA)
                    try:
                        AthlatesClassI["DNA-Tumor"][2] = AthlatesClassITumorHLA[0]
                        AthlatesClassI["DNA-Tumor"][3] = AthlatesClassITumorHLA[1]
                    except TypeError:
                        print("HLA-B typing for tumor not available")
                        AthlatesClassI["DNA-Tumor"][2] = "HLA-B NA"
                        AthlatesClassI["DNA-Tumor"][3] = "HLA-B NA"
                    
                elif (("Athlates" in D) and ("-T-" in D) and ("HLA-C" in D)):
                    print("this is Athlates C typing tumor file")
                    AthlatesClassITumorHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassITumorHLA)
                    try:
                        AthlatesClassI["DNA-Tumor"][4] = AthlatesClassITumorHLA[0]
                        AthlatesClassI["DNA-Tumor"][5] = AthlatesClassITumorHLA[1]
                    except TypeError:
                        print("HLA-C typing for tumor not available")
                        AthlatesClassI["DNA-Tumor"][4] = "HLA-C NA"
                        AthlatesClassI["DNA-Tumor"][5] = "HLA-C NA"
    return [AthlatesClassI]