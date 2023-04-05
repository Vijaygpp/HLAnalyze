import pandas as pd

#Find consensus HLA intrapatient. Polysolver Class I
def getconsensusPolysolverClassI(PolysolverNormalTumorRNA):
    PolysolverNormalTumorRNA_Consensus = set()
    PolysolverNormalTumorRNA_NTR = set.intersection(set(PolysolverNormalTumorRNA["DNA-Normal"]), set(PolysolverNormalTumorRNA["DNA-Tumor"]), set(PolysolverNormalTumorRNA["RNA-Tumor"]))
    print("PolysolverNormalTumorRNA_NTR", PolysolverNormalTumorRNA_NTR)
    PolysolverNormalTumorRNA_Consensus = set.union(PolysolverNormalTumorRNA_Consensus, PolysolverNormalTumorRNA_NTR)
    type(PolysolverNormalTumorRNA_NTR)
    print("Common HLA (PolysolverNormalTumorRNADNA-Normal, PolysolverNormalTumorRNADNA-Tumor, PolysolverNormalTumorRNARNA-Tumor):", set.intersection(set(PolysolverNormalTumorRNA["DNA-Normal"]), set(PolysolverNormalTumorRNA["DNA-Tumor"]), set(PolysolverNormalTumorRNA["RNA-Tumor"])))

    PolysolverNormalTumorRNA_NT = set.intersection(set(PolysolverNormalTumorRNA["DNA-Normal"]), set(PolysolverNormalTumorRNA["DNA-Tumor"]))
    print("PolysolverNormalTumorRNA_NT", PolysolverNormalTumorRNA_NT)
    PolysolverNormalTumorRNA_Consensus = set.union(PolysolverNormalTumorRNA_Consensus, PolysolverNormalTumorRNA_NT)
    type(PolysolverNormalTumorRNA_NT)
    print("Common HLA (PolysolverNormalTumorRNADNA-Normal, PolysolverNormalTumorRNADNA-Tumor):", set.intersection(set(PolysolverNormalTumorRNA["DNA-Normal"]), set(PolysolverNormalTumorRNA["DNA-Tumor"])))

    PolysolverNormalTumorRNA_TR = set.intersection(set(PolysolverNormalTumorRNA["DNA-Tumor"]), set(PolysolverNormalTumorRNA["RNA-Tumor"]))
    print("PolysolverNormalTumorRNA_TR", PolysolverNormalTumorRNA_TR)
    PolysolverNormalTumorRNA_Consensus = set.union(PolysolverNormalTumorRNA_Consensus, PolysolverNormalTumorRNA_TR)
    type(PolysolverNormalTumorRNA_TR)
    print("Common HLA (PolysolverNormalTumorRNADNA-Tumor, PolysolverNormalTumorRNARNA-Tumor):", set.intersection(set(PolysolverNormalTumorRNA["DNA-Tumor"]), set(PolysolverNormalTumorRNA["RNA-Tumor"])))

    PolysolverNormalTumorRNA_NR = set.intersection(set(PolysolverNormalTumorRNA["DNA-Normal"]), set(PolysolverNormalTumorRNA["RNA-Tumor"]))
    print("PolysolverNormalTumorRNA_NR", PolysolverNormalTumorRNA_NR)
    PolysolverNormalTumorRNA_Consensus = set.union(PolysolverNormalTumorRNA_Consensus, PolysolverNormalTumorRNA_NR)
    type(PolysolverNormalTumorRNA_NR)
    print("Common HLA (PolysolverNormalTumorRNADNA-Normal, PolysolverNormalTumorRNARNA-Tumor):", set.intersection(set(PolysolverNormalTumorRNA["DNA-Normal"]), set(PolysolverNormalTumorRNA["RNA-Tumor"])))
    print("PolysolverNormalTumorRNA_Consensus", sorted(PolysolverNormalTumorRNA_Consensus))

    return [PolysolverNormalTumorRNA_Consensus]