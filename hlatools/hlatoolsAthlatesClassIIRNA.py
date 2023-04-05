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
                if (("Athlates" in D) and ("-R-" in D) and ("HLA-DPA1" in D)):
                    print("this is Athlates HLA-DPA1 typing rna file")
                    AthlatesClassIIRNAHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIIRNAHLA)
                    try:
                        AthlatesClassII["RNA-Tumor"][0] = AthlatesClassIIRNAHLA[0]
                        AthlatesClassII["RNA-Tumor"][1] = AthlatesClassIIRNAHLA[1]
                    except TypeError:
                        print("HLA DPA1 typing for RNA not available")
                        AthlatesClassII["RNA-Tumor"][0] = ""
                        AthlatesClassII["RNA-Tumor"][1] = ""

                elif (("Athlates" in D) and ("-R-" in D) and ("HLA-DPB1" in D)):
                    print("this is Athlates HLA-DPB1 typing rna file")
                    AthlatesClassIIRNAHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIIRNAHLA)
                    try:
                        AthlatesClassII["RNA-Tumor"][2] = AthlatesClassIIRNAHLA[0]
                        AthlatesClassII["RNA-Tumor"][3] = AthlatesClassIIRNAHLA[1]
                    except TypeError:
                        print("HLA DPB1 typing for RNA not available")
                        AthlatesClassII["RNA-Tumor"][2] = "DPB1 NA"
                        AthlatesClassII["RNA-Tumor"][3] = "DPB1 NA"

                elif (("Athlates" in D) and ("-R-" in D) and ("HLA-DQA1" in D)):
                    print("this is Athlates HLA-DQA1 typing rna file")
                    AthlatesClassIIRNAHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIIRNAHLA)
                    try:
                        AthlatesClassII["RNA-Tumor"][4] = AthlatesClassIIRNAHLA[0]
                        AthlatesClassII["RNA-Tumor"][5] = AthlatesClassIIRNAHLA[1]
                    except TypeError:
                        print("HLA DQA1 typing for RNA not available")
                        AthlatesClassII["RNA-Tumor"][4] = "DQA1 NA"
                        AthlatesClassII["RNA-Tumor"][5] = "DQA1 NA"
                    
                elif (("Athlates" in D) and ("-R-" in D) and ("HLA-DQB1" in D)):
                    print("this is Athlates HLA-DQB1 typing rna file")
                    AthlatesClassIIRNAHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIIRNAHLA)
                    try:
                        AthlatesClassII["RNA-Tumor"][6] = AthlatesClassIIRNAHLA[0]
                        AthlatesClassII["RNA-Tumor"][7] = AthlatesClassIIRNAHLA[1]
                    except TypeError:
                        print("HLA DQB1 typing for RNA not available")
                        AthlatesClassII["RNA-Tumor"][6] = "DQB1 NA"
                        AthlatesClassII["RNA-Tumor"][7] = "DQB1 NA"
                                    
                elif (("Athlates" in D) and ("-R-" in D) and ("HLA-DRA" in D)):
                    print("this is Athlates HLA-DRA typing rna file")
                    AthlatesClassIIRNAHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIIRNAHLA)
                    try:
                        AthlatesClassII["RNA-Tumor"][8] = AthlatesClassIIRNAHLA[0]
                        AthlatesClassII["RNA-Tumor"][9] = AthlatesClassIIRNAHLA[1]
                    except TypeError:
                        print("HLA DRA typing for RNA not available")
                        AthlatesClassII["RNA-Tumor"][8] = "DRA NA"
                        AthlatesClassII["RNA-Tumor"][9] = "DRA NA"

                elif (("Athlates" in D) and ("-R-" in D) and ("HLA-DRB1" in D)):
                    print("this is Athlates HLA-DRB1 typing rna file")
                    AthlatesClassIIRNAHLA = athlatesclassIIparser.AthlatesClassIIHLAParser(CWD, CurrDir, T, D)
                    print(AthlatesClassIIRNAHLA)
                    try:
                        AthlatesClassII["RNA-Tumor"][10] = AthlatesClassIIRNAHLA[0]
                        AthlatesClassII["RNA-Tumor"][11] = AthlatesClassIIRNAHLA[1]
                    except TypeError:
                        print("HLA DRB1 typing for RNA not available")
                        AthlatesClassII["RNA-Tumor"][10] = "DRB1 NA"
                        AthlatesClassII["RNA-Tumor"][11] = "DRB1 NA"
    return [AthlatesClassII]