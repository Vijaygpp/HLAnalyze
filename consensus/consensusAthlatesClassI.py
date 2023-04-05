#Find consensus HLA intrapatient. Athlates Class I
import pandas as pd

def getconsensusAthlatesClassI(AthlatesClassI):
    AthlatesClassI_Consensus = set()
    AthlatesClassI_NTR = set.intersection(set(AthlatesClassI["DNA-Normal"]), set(AthlatesClassI["DNA-Tumor"]), set(AthlatesClassI["RNA-Tumor"]))
    print("AthlatesClassI_NTR", AthlatesClassI_NTR)
    AthlatesClassI_Consensus = set.union(AthlatesClassI_Consensus, AthlatesClassI_NTR)
    type(AthlatesClassI_NTR)
    print("Common HLA (AthlatesClassIDNA-Normal, AthlatesClassIDNA-Tumor, AthlatesClassIRNA-Tumor):", set.intersection(set(AthlatesClassI["DNA-Normal"]), set(AthlatesClassI["DNA-Tumor"]), set(AthlatesClassI["RNA-Tumor"])))

    AthlatesClassI_NT = set.intersection(set(AthlatesClassI["DNA-Normal"]), set(AthlatesClassI["DNA-Tumor"]))
    print("AthlatesClassI_NT", AthlatesClassI_NT)
    AthlatesClassI_Consensus = set.union(AthlatesClassI_Consensus, AthlatesClassI_NT)
    type(AthlatesClassI_NT)
    print("Common HLA (AthlatesClassIDNA-Normal, AthlatesClassIDNA-Tumor):", set.intersection(set(AthlatesClassI["DNA-Normal"]), set(AthlatesClassI["DNA-Tumor"])))

    AthlatesClassI_TR = set.intersection(set(AthlatesClassI["DNA-Tumor"]), set(AthlatesClassI["RNA-Tumor"]))
    print("AthlatesClassI_TR", AthlatesClassI_TR)
    AthlatesClassI_Consensus = set.union(AthlatesClassI_Consensus, AthlatesClassI_TR)
    type(AthlatesClassI_TR)
    print("Common HLA (AthlatesClassIDNA-Tumor, AthlatesClassIRNA-Tumor):", set.intersection(set(AthlatesClassI["DNA-Tumor"]), set(AthlatesClassI["RNA-Tumor"])))

    AthlatesClassI_NR = set.intersection(set(AthlatesClassI["DNA-Normal"]), set(AthlatesClassI["RNA-Tumor"]))
    print("AthlatesClassI_NR", AthlatesClassI_NR)
    AthlatesClassI_Consensus = set.union(AthlatesClassI_Consensus, AthlatesClassI_NR)
    type(AthlatesClassI_NR)
    print("Common HLA (AthlatesClassIDNA-Normal, AthlatesClassIRNA-Tumor):", set.intersection(set(AthlatesClassI["DNA-Normal"]), set(AthlatesClassI["RNA-Tumor"])))
    print("AthlatesClassI_Consensus", sorted(AthlatesClassI_Consensus))

    return [AthlatesClassI_Consensus]