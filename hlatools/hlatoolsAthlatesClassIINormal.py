import os as os
import pandas as pd

from parsers import athlatesclassIIparser

def getHLA(CWD, CurrDir, AllHLATools, AthlatesClassII):
    for T in AllHLATools:
    #    print("Directory is" + T)
        if os.path.isdir(os.path.join(CWD, CurrDir, T)) and ("ATHLATES" in T):
            print("HLADIR contains: ", os.listdir(os.path.join(CWD, CurrDir, T)))
            HLADIR = os.listdir(os.path.join(CWD, CurrDir, T))
            for D in HLADIR:
                print(D)
                if (("Athlates" in D) and ("-N-" in D) and ("HLA-DPA1" in D)):
                    print("this is Athlates HLA-DPA1 typing normal file")
                    AthlatesClassIINormalHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIINormalHLA)
                    try:
                        AthlatesClassII["DNA-Normal"][0] = AthlatesClassIINormalHLA[0]
                        AthlatesClassII["DNA-Normal"][1] = AthlatesClassIINormalHLA[1]
                    except TypeError:
                        print("HLA DPA1 typing for Normal not available")
                        AthlatesClassII["DNA-Normal"][0] = "DPA1 NA"
                        AthlatesClassII["DNA-Normal"][1] = "DPA1 NA"

                elif (("Athlates" in D) and ("-N-" in D) and ("HLA-DPB1" in D)):
                    print("this is Athlates HLA-DPB1 typing normal file")
                    AthlatesClassIINormalHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIINormalHLA)
                    try:
                        AthlatesClassII["DNA-Normal"][2] = AthlatesClassIINormalHLA[0]
                        AthlatesClassII["DNA-Normal"][3] = AthlatesClassIINormalHLA[1]
                    except TypeError:
                        print("HLA DPB1 typing for Normal not available")
                        AthlatesClassII["DNA-Normal"][2] = "DPB1 NA"
                        AthlatesClassII["DNA-Normal"][3] = "DPB1 NA"

                elif (("Athlates" in D) and ("-N-" in D) and ("HLA-DQA1" in D)):
                    print("this is Athlates HLA-DQA1 typing normal file")
                    AthlatesClassIINormalHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIINormalHLA)
                    try:
                        AthlatesClassII["DNA-Normal"][4] = AthlatesClassIINormalHLA[0]
                        AthlatesClassII["DNA-Normal"][5] = AthlatesClassIINormalHLA[1]
                    except TypeError:
                        print("HLA DQA1 typing for Normal not available")
                        AthlatesClassII["DNA-Normal"][4] = "DQA1 NA"
                        AthlatesClassII["DNA-Normal"][5] = "DQA1 NA"
                    
                elif (("Athlates" in D) and ("-N-" in D) and ("HLA-DQB1" in D)):
                    print("this is Athlates HLA-DQB1 typing normal file")
                    AthlatesClassIINormalHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIINormalHLA)
                    try:
                        AthlatesClassII["DNA-Normal"][6] = AthlatesClassIINormalHLA[0]
                        AthlatesClassII["DNA-Normal"][7] = AthlatesClassIINormalHLA[1]
                    except TypeError:
                        print("HLA DQB1 typing for Normal not available")
                        AthlatesClassII["DNA-Normal"][6] = "DQB1 NA"
                        AthlatesClassII["DNA-Normal"][7] = "DQB1 NA"

                elif (("Athlates" in D) and ("-N-" in D) and ("HLA-DRA" in D)):
                    print("this is Athlates HLA-DRA typing normal file")
                    AthlatesClassIINormalHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIINormalHLA)
                    try:
                        AthlatesClassII["DNA-Normal"][8] = AthlatesClassIINormalHLA[0]
                        AthlatesClassII["DNA-Normal"][9] = AthlatesClassIINormalHLA[1]
                    except TypeError:
                        print("HLA DRA typing for Normal not available")
                        AthlatesClassII["DNA-Normal"][8] = "DRA NA"
                        AthlatesClassII["DNA-Normal"][9] = "DRA NA"
                                    
                elif (("Athlates" in D) and ("-N-" in D) and ("HLA-DRB1" in D)):
                    print("this is Athlates HLA-DRB1 typing normal file")
                    AthlatesClassIINormalHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIINormalHLA)
                    try:
                        AthlatesClassII["DNA-Normal"][10] = AthlatesClassIINormalHLA[0]
                        AthlatesClassII["DNA-Normal"][11] = AthlatesClassIINormalHLA[1]
                    except TypeError:
                        print("HLA DRB1 typing for Normal not available")
                        AthlatesClassII["DNA-Normal"][10] = "DRB1 NA"
                        AthlatesClassII["DNA-Normal"][11] = "DRB1 NA"
    return [AthlatesClassII]