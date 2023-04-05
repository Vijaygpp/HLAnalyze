import pandas as pd

#Find consensus HLA intrapatient. OptiType Class I
def getconsensusOptitypeClassI(OptiTypeNormalTumorRNA):
    OptiTypeNormalTumorRNA_Consensus = set()
    OptiTypeNormalTumorRNA_NTR = set.intersection(set(OptiTypeNormalTumorRNA["DNA-Normal"]), set(OptiTypeNormalTumorRNA["DNA-Tumor"]), set(OptiTypeNormalTumorRNA["RNA-Tumor"]))
    print("OptiTypeNormalTumorRNA_NTR", OptiTypeNormalTumorRNA_NTR)
    OptiTypeNormalTumorRNA_Consensus = set.union(OptiTypeNormalTumorRNA_Consensus, OptiTypeNormalTumorRNA_NTR)
    type(OptiTypeNormalTumorRNA_NTR)
    print("Common HLA (OptiTypeNormalTumorRNADNA-Normal, OptiTypeNormalTumorRNADNA-Tumor, OptiTypeNormalTumorRNARNA-Tumor):", set.intersection(set(OptiTypeNormalTumorRNA["DNA-Normal"]), set(OptiTypeNormalTumorRNA["DNA-Tumor"]), set(OptiTypeNormalTumorRNA["RNA-Tumor"])))

    OptiTypeNormalTumorRNA_NT = set.intersection(set(OptiTypeNormalTumorRNA["DNA-Normal"]), set(OptiTypeNormalTumorRNA["DNA-Tumor"]))
    print("OptiTypeNormalTumorRNA_NT", OptiTypeNormalTumorRNA_NT)
    OptiTypeNormalTumorRNA_Consensus = set.union(OptiTypeNormalTumorRNA_Consensus, OptiTypeNormalTumorRNA_NT)
    type(OptiTypeNormalTumorRNA_NT)
    print("Common HLA (OptiTypeNormalTumorRNADNA-Normal, OptiTypeNormalTumorRNADNA-Tumor):", set.intersection(set(OptiTypeNormalTumorRNA["DNA-Normal"]), set(OptiTypeNormalTumorRNA["DNA-Tumor"])))

    OptiTypeNormalTumorRNA_TR = set.intersection(set(OptiTypeNormalTumorRNA["DNA-Tumor"]), set(OptiTypeNormalTumorRNA["RNA-Tumor"]))
    print("OptiTypeNormalTumorRNA_TR", OptiTypeNormalTumorRNA_TR)
    OptiTypeNormalTumorRNA_Consensus = set.union(OptiTypeNormalTumorRNA_Consensus, OptiTypeNormalTumorRNA_TR)
    type(OptiTypeNormalTumorRNA_TR)
    print("Common HLA (OptiTypeNormalTumorRNADNA-Tumor, OptiTypeNormalTumorRNARNA-Tumor):", set.intersection(set(OptiTypeNormalTumorRNA["DNA-Tumor"]), set(OptiTypeNormalTumorRNA["RNA-Tumor"])))

    OptiTypeNormalTumorRNA_NR = set.intersection(set(OptiTypeNormalTumorRNA["DNA-Normal"]), set(OptiTypeNormalTumorRNA["RNA-Tumor"]))
    print("OptiTypeNormalTumorRNA_NR", OptiTypeNormalTumorRNA_NR)
    OptiTypeNormalTumorRNA_Consensus = set.union(OptiTypeNormalTumorRNA_Consensus, OptiTypeNormalTumorRNA_NR)
    type(OptiTypeNormalTumorRNA_NR)
    print("Common HLA (OptiTypeNormalTumorRNADNA-Normal, OptiTypeNormalTumorRNARNA-Tumor):", set.intersection(set(OptiTypeNormalTumorRNA["DNA-Normal"]), set(OptiTypeNormalTumorRNA["RNA-Tumor"])))
    print("OptiTypeNormalTumorRNA_Consensus", sorted(OptiTypeNormalTumorRNA_Consensus))

    return [OptiTypeNormalTumorRNA_Consensus]