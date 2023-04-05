import pandas as pd

#Find consensus HLA intrapatient. Athlates Class II
def getconsensusAthlatesClassII(AthlatesClassII):
    AthlatesClassII_Consensus = set()
    AthlatesClassII_NTR = set.intersection(set(AthlatesClassII["DNA-Normal"]), set(AthlatesClassII["DNA-Tumor"]), set(AthlatesClassII["RNA-Tumor"]))
    print("AthlatesClassII_NTR", AthlatesClassII_NTR)
    AthlatesClassII_Consensus = set.union(AthlatesClassII_Consensus, AthlatesClassII_NTR)
    type(AthlatesClassII_NTR)
    print("Common HLA (AthlatesClassIIDNA-Normal, AthlatesClassIIDNA-Tumor, AthlatesClassIIRNA-Tumor):", set.intersection(set(AthlatesClassII["DNA-Normal"]), set(AthlatesClassII["DNA-Tumor"]), set(AthlatesClassII["RNA-Tumor"])))

    AthlatesClassII_NT = set.intersection(set(AthlatesClassII["DNA-Normal"]), set(AthlatesClassII["DNA-Tumor"]))
    print("AthlatesClassII_NT", AthlatesClassII_NT)
    AthlatesClassII_Consensus = set.union(AthlatesClassII_Consensus, AthlatesClassII_NT)
    type(AthlatesClassII_NT)
    print("Common HLA (AthlatesClassIIDNA-Normal, AthlatesClassIIDNA-Tumor):", set.intersection(set(AthlatesClassII["DNA-Normal"]), set(AthlatesClassII["DNA-Tumor"])))

    AthlatesClassII_TR = set.intersection(set(AthlatesClassII["DNA-Tumor"]), set(AthlatesClassII["RNA-Tumor"]))
    print("AthlatesClassII_TR", AthlatesClassII_TR)
    AthlatesClassII_Consensus = set.union(AthlatesClassII_Consensus, AthlatesClassII_TR)
    type(AthlatesClassII_TR)
    print("Common HLA (AthlatesClassIIDNA-Tumor, AthlatesClassIIRNA-Tumor):", set.intersection(set(AthlatesClassII["DNA-Tumor"]), set(AthlatesClassII["RNA-Tumor"])))

    AthlatesClassII_NR = set.intersection(set(AthlatesClassII["DNA-Normal"]), set(AthlatesClassII["RNA-Tumor"]))
    print("AthlatesClassII_NR", AthlatesClassII_NR)
    AthlatesClassII_Consensus = set.union(AthlatesClassII_Consensus, AthlatesClassII_NR)
    type(AthlatesClassII_NR)
    print("Common HLA (AthlatesClassIIDNA-Normal, AthlatesClassIIRNA-Tumor):", set.intersection(set(AthlatesClassII["DNA-Normal"]), set(AthlatesClassII["RNA-Tumor"])))

    print("AthlatesClassII_Consensus", sorted(AthlatesClassII_Consensus))
    
    return [AthlatesClassII_Consensus]