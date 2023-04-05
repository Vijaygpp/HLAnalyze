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
                if (("Athlates" in D) and ("-T-" in D) and ("HLA-DPA1" in D)):
                    print("this is Athlates HLA-DPA1 typing tumor file")
                    AthlatesClassIITumorHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIITumorHLA)
                    try:
                        AthlatesClassII["DNA-Tumor"][0] = AthlatesClassIITumorHLA[0]
                        AthlatesClassII["DNA-Tumor"][1] = AthlatesClassIITumorHLA[1]
                    except TypeError:
                        print("HLA DPA1 typing for tumor not available")
                        AthlatesClassII["DNA-Tumor"][0] = "DPA1 NA"
                        AthlatesClassII["DNA-Tumor"][1] = "DPA1 NA"
     
                elif (("Athlates" in D) and ("-T-" in D) and ("HLA-DPB1" in D)):
                    print("this is Athlates HLA-DPB1 typing tumor file")
                    AthlatesClassIITumorHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIITumorHLA)
                    try:
                        AthlatesClassII["DNA-Tumor"][2] = AthlatesClassIITumorHLA[0]
                        AthlatesClassII["DNA-Tumor"][3] = AthlatesClassIITumorHLA[1]
                    except TypeError:
                        print("HLA DPB1 typing for tumor not available")
                        AthlatesClassII["DNA-Tumor"][2] = "DPB1 NA"
                        AthlatesClassII["DNA-Tumor"][3] = "DPB1 NA"

                elif (("Athlates" in D) and ("-T-" in D) and ("HLA-DQA1" in D)):
                    print("this is Athlates HLA-DQA1 typing tumor file")
                    AthlatesClassIITumorHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIITumorHLA)
                    try:
                        AthlatesClassII["DNA-Tumor"][4] = AthlatesClassIITumorHLA[0]
                        AthlatesClassII["DNA-Tumor"][5] = AthlatesClassIITumorHLA[1]
                    except TypeError:
                        print("HLA DQA1 typing for tumor not available")
                        AthlatesClassII["DNA-Tumor"][4] = "DQA1 NA"
                        AthlatesClassII["DNA-Tumor"][5] = "DQA1 NA"
                        
                elif (("Athlates" in D) and ("-T-" in D) and ("HLA-DQB1" in D)):
                    print("this is Athlates HLA-DQB1 typing tumor file")
                    AthlatesClassIITumorHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIITumorHLA)
                    try:
                        AthlatesClassII["DNA-Tumor"][6] = AthlatesClassIITumorHLA[0]
                        AthlatesClassII["DNA-Tumor"][7] = AthlatesClassIITumorHLA[1]
                    except TypeError:
                        print("HLA DQB1 typing for tumor not available")
                        AthlatesClassII["DNA-Tumor"][6] = "DQB1 NA"
                        AthlatesClassII["DNA-Tumor"][7] = "DQB1 NA"

                elif (("Athlates" in D) and ("-T-" in D) and ("HLA-DRA" in D)):
                    print("this is Athlates HLA-DRA typing tumor file")
                    AthlatesClassIITumorHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIITumorHLA)
                    try:
                        AthlatesClassII["DNA-Tumor"][8] = AthlatesClassIITumorHLA[0]
                        AthlatesClassII["DNA-Tumor"][9] = AthlatesClassIITumorHLA[1]
                    except TypeError:
                        print("HLA DRA typing for tumor not available")
                        AthlatesClassII["DNA-Tumor"][8] = "DRA NA"
                        AthlatesClassII["DNA-Tumor"][9] = "DRA NA"
                                    
                elif (("Athlates" in D) and ("-T-" in D) and ("HLA-DRB1" in D)):
                    print("this is Athlates HLA-DRB1 typing tumor file")
                    AthlatesClassIITumorHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIITumorHLA)
                    try:
                        AthlatesClassII["DNA-Tumor"][10] = AthlatesClassIITumorHLA[0]
                        AthlatesClassII["DNA-Tumor"][11] = AthlatesClassIITumorHLA[1]
                    except TypeError:
                        print("HLA DRB1 typing for tumor not available")
                        AthlatesClassII["DNA-Tumor"][10] = "DRB1 NA"
                        AthlatesClassII["DNA-Tumor"][11] = "DRB1 NA"
    return [AthlatesClassII]