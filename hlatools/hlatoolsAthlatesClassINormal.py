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
                if (("Athlates" in D) and ("-N-" in D) and ("HLA-A" in D)):
                    print("this is Athlates A typing normal file") #Code was here
                    AthlatesClassINormalHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassINormalHLA)
                    try:
                        AthlatesClassI["DNA-Normal"][0] = AthlatesClassINormalHLA[0]
                        AthlatesClassI["DNA-Normal"][1] = AthlatesClassINormalHLA[1]
                    except TypeError:
                        print("HLA-A typing for Normal not available")
                        AthlatesClassI["DNA-Normal"][0] = "HLA-A NA"
                        AthlatesClassI["DNA-Normal"][1] = "HLA-A NA"
                        
                elif (("Athlates" in D) and ("-N-" in D) and ("HLA-B" in D)):
                    print("this is Athlates B typing normal file")
                    AthlatesClassINormalHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassINormalHLA)
                    try:
                        AthlatesClassI["DNA-Normal"][2] = AthlatesClassINormalHLA[0]
                        AthlatesClassI["DNA-Normal"][3] = AthlatesClassINormalHLA[1]
                    except TypeError:
                        print("HLA-B typing for Normal not available")
                        AthlatesClassI["DNA-Normal"][2] = "HLA-B NA"
                        AthlatesClassI["DNA-Normal"][3] = "HLA-B NA"
                    
                elif (("Athlates" in D) and ("-N-" in D) and ("HLA-C" in D)):
                    print("this is Athlates C typing normal file")
                    AthlatesClassINormalHLA = athlatesclassIparser.AthlatesClassIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassINormalHLA)
                    try:
                        AthlatesClassI["DNA-Normal"][4] = AthlatesClassINormalHLA[0]
                        AthlatesClassI["DNA-Normal"][5] = AthlatesClassINormalHLA[1]
                    except TypeError:
                        print("HLA-C typing for Normal not available")
                        AthlatesClassI["DNA-Normal"][4] = "HLA-C NA"
                        AthlatesClassI["DNA-Normal"][5] = "HLA-C NA"

    return [AthlatesClassI]